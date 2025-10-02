import pandas as pd
from logger import get_logger

logger = get_logger(__name__)

def extract_from_csv(file_path):
    #ES: Extrae el archivo csv
    #EN: Extracts a csv file
    if not os.path.exists(file_path):
        logger.error("Extrayendo %s", inspect.getdoc(file_path))
        raise FileNotFoundError(f"Archivo no encontrado: {file_path}")
    
    logger.debug("Extrayendo archivo CSV desde: %s (abs: %s)",
                file_path, os.path.abspath(file_path))
    return pd.read_csv(file_path) 
