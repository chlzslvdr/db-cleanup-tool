import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(project_root)

from utils.db_utils import delete_from_db, load_ids

if __name__ == "__main__":
    ids_to_delete = load_ids("data/employer_id.csv")

    tables = [
        "banner_images", "leaders", "webinars", "videos",
        "images", "member_invites", "employer_users",
        "employer_verifications", "employers"
    ]

    # Perform deletion for each table
    for table in tables:
        delete_from_db("psql_employers_profile_db", table, "employer_id", ids_to_delete)
