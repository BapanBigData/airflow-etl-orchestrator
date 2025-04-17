import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/")
COMPANY_NAME = os.getenv("COMPANY_NAME", "AMERICAN EXPRESS COMPANY")
DATA_DIR = os.getenv("DATA_DIR", "/opt/airflow/data/complaints_raw")
