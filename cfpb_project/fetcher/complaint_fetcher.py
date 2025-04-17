import os
from datetime import datetime
import requests
# import logging
from config.config import BASE_URL, COMPANY_NAME

# # ✅ Create logs folder if not present
# os.makedirs("logs", exist_ok=True)

# # ✅ Generate log filename with timestamp
# timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# LOG_PATH = f"logs/fetch_complaints_{timestamp}.log"

# # ✅ Setup logging
# logging.basicConfig(
#     filename=LOG_PATH,
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )


def fetch_complaints(start_date: str, end_date: str):
    # logging.info(
    #     f"Fetching complaints from {start_date} to {end_date} for {COMPANY_NAME}")
    print(f"Fetching complaints from {start_date} to {end_date} for {COMPANY_NAME}")

    params = {
        # 'company': COMPANY_NAME,
        'date_received_min': start_date,
        'date_received_max': end_date,
        'format': 'json'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        # logging.info(f"✅ Retrieved {len(data)} complaints")
        print(f"✅ Retrieved {len(data)} complaints")
        return data
    except Exception as e:
        # logging.error(f"❌ Failed to fetch complaints: {str(e)}")
        print(f"❌ Failed to fetch complaints: {str(e)}")
        raise
