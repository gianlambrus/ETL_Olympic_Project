import pandas as pd
from logger import get_logger

logger = get_logger(__name__)

def extract_from_csv(file_path):
    #ES: Extrae el archivo csv
    #EN: Extracts a csv file
    logger.debug(f"Extrayendo {file_path}")
    return pd.read_csv(file_path)
