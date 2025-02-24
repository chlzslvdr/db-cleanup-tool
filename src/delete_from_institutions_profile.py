import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(project_root)

from utils.db_utils import delete_from_db, load_ids

if __name__ == "__main__":
    ids_to_delete = load_ids("data/institution_id.csv")

    tables = [
        "institution_banners", "institution_images", "institution_leader_quotes",
        "institution_logos", "institution_users", "institutions"
    ]

    # Perform deletion for each table
    for table in tables:
        delete_from_db("psql_institutions_profile_db", table, "institution_id", ids_to_delete)
