import pandas as pd
from logger import get_logger

logger = get_logger(__name__)

def extract_from_csv(file_path):
    logger.info(f"Extrayendo {file_path}")
    return pd.read_csv(file_path)
