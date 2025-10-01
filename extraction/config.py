import os
from pathlib import Path
from dotenv import load_dotenv

base_dir = Path(__file__).resolve().parent.parent
env_path = base_dir / ".env"

if env_path.exists():
    load_dotenv(dotenv_path=env_path)
else:
    load_dotenv()

olympic_raw_path = os.getenv("olympic_raw_path", str(base_dir / "data" / "olympics.csv"))
bronze_path = os.getenv("bronze_path", str(base_dir / "datalake" / "bronze"))
silver_path = os.getenv("silver_path", str(base_dir / "datalake" / "silver"))
gold_path = os.getenv("gold_path", str(base_dir / "datalake" / "gold"))
