import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(project_root)

from utils.db_utils import delete_from_db, load_ids

if __name__ == "__main__":
    ids_to_delete = load_ids("data/employer_id.csv")

    tables = [
        "candidate_skills", "candidates", "draft_job_skills", "draft_jobs",
        "job_interview_schedules", "job_skills", "jobs", "job_employers"
    ]

    # Perform deletion for each table
    for table in tables:
        print(table)
        delete_from_db("psql_job_postings_db", table, "employer_id", ids_to_delete)
