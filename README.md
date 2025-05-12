# YouTube Trending Data ETL Pipeline

This project implements a complete ETL (Extract, Transform, Load) pipeline using the YouTube Data API. The pipeline extracts trending video data, transforms it by calculating key engagement metrics, and loads the cleaned data into a PostgreSQL database. The pipeline is automated using Airflow for scheduling and orchestration.

# Project Overview

Data Source: YouTube Data API (Trending Videos)
Transformation:
- Cleaning and type conversion of numeric fields.
- Calculating a new feature: engagement_rate based on likes and comments.
Data Destination: PostgreSQL Database (youtube_etl), Table: trending_videos.
Automation: Orchestrated using Apache Airflow with a daily scheduled DAG.

## Technologies Used

Python 3.11
Pandas
SQLAlchemy
PostgreSQL
Apache Airflow
Google API Client
Docker (optional for containerization)

## Project Structure

690A Final/
├── dags/
│   └── etl_dag.py
├── extract/
│   └── extract_data.py
├── transform/
│   └── transform_data.py
├── load/
│   └── load_data.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

# Setup Instructions

1) Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2) Set Up the Virtual Environment
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3) Configure Environment Variables
Copy the .env.example file and create your own .env file:
cp .env.example .env
Fill in the actual values in .env:
API_KEY=your_youtube_api_key
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=youtube_etl

4) Run the ETL Pipeline Manually
python extract/extract_data.py
python transform/transform_data.py
python load/load_data.py

5) Automation with Airflow
Initialize Airflow:
export AIRFLOW_HOME=~/airflow
airflow db init
airflow users create --username admin --firstname YourName --lastname LastName --role Admin --email your_email@example.com --password admin
Start Airflow:
airflow webserver --port 8080
airflow scheduler
Access Airflow at http://localhost:8080 and trigger the youtube_trending_etl DAG.

# Notes

.env is excluded from version control for security reasons.
.env.example provides a template for environment variable configuration.
The pipeline is scheduled to run daily via Airflow but can be adjusted in etl_dag.py.

# Challenges & Lessons Learned

- Faced compatibility issues using Python 3.13 with critical libraries like Pandas and Airflow. Solved by switching to the more stable Python 3.11.
- Learned the importance of isolating environment configurations using .env files and keeping sensitive data out of version control.
- Gained hands-on experience orchestrating automated data pipelines with Airflow, including scheduling, error handling, and dependency management.
- Resolved package conflicts by properly managing dependencies and versions through a clean requirements.txt.
- Developed a better understanding of professional project organization using .gitignore, .env.example, and modularized code structures.