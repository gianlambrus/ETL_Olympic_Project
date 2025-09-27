import os
from dotenv import load_dotenv

load_dotenv()

datalake_base = os.getenv("DATALAKE_BASE")
olympic_raw_path = os.getenv("OLYMPIC_RAW_PATH")
bronze_path = os.getenv("BRONZE_PATH")
silver_path = os.getenv("SILVER_PATH")
gold_path = os.getenv("GOLD_PATH")