import os
from dotenv import load_dotenv

load_dotenv()

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

datalake_path = os.path.join(base_dir, "datalake")

olympic_raw_path = os.getenv("olympic_raw_path", os.path.join(base_dir, "olympics.csv"))
bronze_path = os.getenv("bronze_path", os.path.join(datalake_path, "bronze"))
silver_path = os.getenv("silver_path", os.path.join(datalake_path, "silver"))
gold_path = os.getenv("gold_path", os.path.join(datalake_path, "gold"))