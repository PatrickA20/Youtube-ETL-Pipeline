from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

#Fix import paths for Airflow
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from extract.extract_data import extract_trending_videos
from transform.transform_data import transform_data
from load.load_data import load_data_to_postgres

default_args = {
    'owner': 'patricka20',
    'depends_on_past': False,
    'email': ['your_email@example.com'],  # Optional
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def etl_process():
    df_extracted = extract_trending_videos(region_code='US', max_results=50)
    df_transformed = transform_data(df_extracted)
    load_data_to_postgres(df_transformed, 'trending_videos')

with DAG(
    'youtube_trending_etl',
    default_args=default_args,
    description='ETL pipeline for YouTube trending data',
    schedule='@daily',  #Could change this to test more frequently: '*/5 * * * *'
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['etl', 'youtube'],
) as dag:

    run_etl = PythonOperator(
        task_id='run_etl_process',
        python_callable=etl_process
    )

    run_etl
