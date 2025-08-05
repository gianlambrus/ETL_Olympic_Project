from Config import olympics_raw_path
import pandas as pd

def extract_from_csv(file_path):
    return pd.read_csv(file_path)
