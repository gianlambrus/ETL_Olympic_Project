from Config import olympics_raw_path
import pandas as pd

def extract_from_csv(df):
    return pd.read_csv(df)
