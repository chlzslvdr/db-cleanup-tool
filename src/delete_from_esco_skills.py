import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(project_root)

from utils.db_utils import delete_from_db, load_ids

if __name__ == "__main__":
    employer_ids_to_delete = load_ids("data/employer_id.csv")
    employer_tables = [
        "employer_job_skills", "employer_job_occupations"
    ]

    # Delete from employer-related tables
    for table in employer_tables:
        delete_from_db("psql_esco_skills_db", table, "employer_id", employer_ids_to_delete)

    jobseeker_ids_to_delete = load_ids("data/job_seeker_id.csv")
    jobseeker_tables = [
        "job_seeker_skills", "job_seeker_occupations"
    ]

    # Delete from jobseeker-related tables
    for table in jobseeker_tables:
        delete_from_db("psql_esco_skills_db", table, "job_seeker_id", jobseeker_ids_to_delete)
