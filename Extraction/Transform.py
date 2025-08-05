import os
import pandas as pd
import pyarrow as pa
from Extract import extract_from_csv
from Config import olympic_raw_path, bronze_path, silver_path
df_bronze_olympic = extract_from_csv(olympic_raw_path)


def rename_columns(df):
    rename_mapping = {
                    '0':'Paises',
                    '1':'Total summer games',
                    '2':'Gold medals',
                    '3':'Silver medals',
                    '4':'Bronze medals',
                    '5':'Summer totals',
                    '6':'Total winter games',
                    '7':'Gold medals',
                    '8':'Silver medals',
                    '9':'Bronze medals',
                    '10':'Winter totals',
                    '11':'Total games',
                    '12':'Gold',
                    '13':'Silver',
                    '14':'Bronze',
                    '15':'Total medals'
                    }
    df = df.rename(columns = rename_mapping)
    return df  


def clean_columns(df):
    df = df.drop(index=0)
    return df


def change_values(df):
    type_mapping = {
        'Paises':'object',
        'Total summer games':'int64',
        'Gold medals':'int64',
        'Silver medals':'int64',
        'Bronze medals':'int64',
        'Summer totals':'int64',
        'Total winter games':'int64',
        'Gold medals':'int64',
        'Silver medals':'int64',
        'Bronze medals':'int64',
        'Winter totals':'int64',
        'Total games':'int64',
        'Gold':'int64',
        'Silver':'int64',
        'Bronze':'int64',
        'Total medals':'int64'        
        } 
    df = df.astype(type_mapping)
    return df 

df_silver_olympic = rename_columns(df_bronze_olympic)
df_silver_olympic = clean_columns(df_silver_olympic)
df_silver_olympic = change_values(df_silver_olympic)