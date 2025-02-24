# db-cleanup-tool

Python tool for deleting records from a PostgreSQL database using IDs listed in a CSV file

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

1. **Python 3.x** (Python 3.6 or higher recommended).
2. **PostgreSQL Database** running and accessible.
3. **Required Python libraries** (installed via `requirements.txt`).

### Installing Dependencies

Clone the repository and install the required dependencies by running:

```bash
git clone git@github.com:wanpng/db-cleanup-tool.git
cd db-cleanup-tool
pip install -r requirements.txt
```

### Environment Variables
Example `.env` file:

```
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
```

### Usage

- Add the IDs to be deleted in their respective CSV file in `data` folder
```
data/employer_id.csv
data/job_seeker_id.csv
data/institution_id.csv
```

Note: NEVER commit the IDs in the data folder.

- Delete Data From Job Postings DB
```
python3 src/delete_from_job_postings.py
```

- Delete Data From Employers Profile DB
```
python3 src/delete_from_employers_profile.py
```

- Delete Data From Jobseekers Profile DB
```
python3 src/delete_from_job_seekers_profile.py
```

- Delete Data From ESCO Skills DB
```
python3 src/delete_from_esco_skills.py
```

- Delete Data From Institutions Profile DB
```
python3 src/delete_from_institutions_profile.py
```