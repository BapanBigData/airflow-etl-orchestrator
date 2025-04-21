import os
# import logging
import pandas as pd
from datetime import datetime, timedelta
from fetcher.complaint_fetcher import fetch_complaints
from config.config import DATA_DIR

# # ✅ Create logs folder if not present
# os.makedirs("logs", exist_ok=True)

# # ✅ Generate log filename with timestamp
# timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# LOG_PATH = f"logs/daily_job_{timestamp}.log"

# # ✅ Setup logging
# logging.basicConfig(
#     filename=LOG_PATH,
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

def run_daily_task():
    today = datetime.today()
    end_date_api = today.strftime('%Y-%m-%d')                # for API
    end_date_file = today.strftime('%Y-%m-%d_%H_%M')         # for filename
    start_date = (today - timedelta(days=(90))).strftime('%Y-%m-%d')

    # logging.info(f"🚀 Starting daily fetch from {start_date} to {end_date_api}")
    print(f"🚀 Starting daily fetch from {start_date} to {end_date_api}")
    

    try:
        data = fetch_complaints(start_date, end_date_api)

        if not data or not isinstance(data, list):
            # logging.warning("⚠️ No data found or unexpected response format.")
            print("⚠️ No data found or unexpected response format.")
            return

        complaints = [item["_source"] for item in data if "_source" in item]

        if not complaints:
            # logging.info("ℹ️ No complaint records found after filtering.")
            print("ℹ️ No complaint records found after filtering.")
            return

        df = pd.DataFrame(complaints)

        os.makedirs(DATA_DIR, exist_ok=True)

        filename = f"complaints-{start_date}-{end_date_file}.csv"
        filepath = os.path.join(DATA_DIR, filename)
        df.to_csv(filepath, index=False)

        # logging.info(f"✅ Saved {len(df)} complaints to {filepath}")
        print(f"✅ Saved {len(df)} complaints to {filepath}")

    except Exception as e:
        # logging.error(f"❌ run_daily_task failed: {str(e)}", exc_info=True)
        print(f"❌ run_daily_task failed: {str(e)}", exc_info=True)
