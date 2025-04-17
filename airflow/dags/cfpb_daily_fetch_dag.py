import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv

# ✅ This is correct:
sys.path.append('/opt/airflow/cfpb_project')
load_dotenv('/opt/airflow/cfpb_project/.env')

# ✅ Fix this line:
from scheduler.daily_job import run_daily_task

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
}

with DAG(
    dag_id='cfpb_daily_fetch',
    default_args=default_args,
    description='Daily fetch of CFPB complaints',
    start_date=datetime(2024, 12, 15),   
    schedule_interval="0 23 * * 1-5" ,         
    catchup=False,
    tags=['dev']
) as dag:

    fetch_task = PythonOperator(
        task_id='run_cfpb_fetch',
        python_callable=run_daily_task
    )
