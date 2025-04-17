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
    dag_id='cfpb_daily_fetch_auto_tr',
    default_args=default_args,
    description='Daily fetch of CFPB complaints',
    # Set start_date in UTC: For 9:00 AM IST, use 03:30 AM UTC
    start_date=datetime(2025, 4, 17, 3, 30),   
    # triggers every day at 4:30 PM IST
    schedule_interval="0 11 * * *" ,         
    catchup=False
) as dag:

    fetch_task = PythonOperator(
        task_id='run_cfpb_fetch_auto_tr',
        python_callable=run_daily_task
    )
