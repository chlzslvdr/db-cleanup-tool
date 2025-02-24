import psycopg2
import os
import csv
import uuid
from dotenv import load_dotenv
from psycopg2 import sql

load_dotenv()

def get_db_connection(db_name):
    """Establishes and returns a connection to the PostgreSQL database."""
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=5432
        )
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
    
def load_ids(file_path):
    """Load IDs from CSV and return them as a list of UUIDs."""
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        return [row[0] for row in csv_reader if row]

def delete_from_db(db_name, table, condition_column, condition_values):
    """Deletes records from the specified table based on a list of condition values."""
    connection = get_db_connection(db_name)
    if connection:
        try:
            cursor = connection.cursor()

            # Convert UUIDs to strings for psycopg2
            condition_values = [str(uuid.UUID(id)) for id in condition_values]

            # Correct query format using PostgreSQL array handling with UUID casting
            query = sql.SQL("DELETE FROM {table} WHERE {column} = ANY(ARRAY[{values}]::uuid[])").format(
                table=sql.Identifier(table),
                column=sql.Identifier(condition_column),
                values=sql.SQL(',').join(map(sql.Literal, condition_values))
            )

            # Execute the query with the list of condition values (as strings)
            cursor.execute(query)
            connection.commit()

            # Print total number of deleted records
            total_deleted = cursor.rowcount
            print(f"Total Deleted records in {table}: {total_deleted}")
            cursor.close()

        except Exception as e:
            print(f"Error deleting data: {e}")
        finally:
            connection.close()
