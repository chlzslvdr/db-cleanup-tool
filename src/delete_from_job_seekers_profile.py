import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(project_root)

from utils.db_utils import delete_from_db, load_ids

if __name__ == "__main__":
    ids_to_delete = load_ids("data/job_seeker_id.csv")

    tables = [
        "job_seeker_skills", "trainings", "affiliations", "educations", 
        "work_experiences", "supporting_documents", "job_seeker_employment_types", 
        "account_verifications", "saved_search_career_levels", 
        "saved_search_employment_types", "saved_search_job_classifications", 
        "saved_searches", "job_seekers"
    ]

    # Perform deletion for each table
    for table in tables:
        delete_from_db("psql_job_seekers_profile_db", table, "job_seeker_id", ids_to_delete)
