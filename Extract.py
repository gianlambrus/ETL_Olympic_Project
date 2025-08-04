import os
import pandas as pd

def extract_from_csv(file_path):
    return pd.read_csv(file_path)

def extract_from_excel(file_path):
    return pd.read_excel(file_path)

file_path = 'D:/Practica_ETL/olympics.csv'