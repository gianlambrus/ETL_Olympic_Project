import os
import pandas as pd
import pyarrow as pa
from Extract import extract_from_csv

def rename_columns(df):
    rename_mapping = {
                    '0':'Paises',
                    '1':'Summer games',
                    '2':'Summer Gold medals',
                    '3':'Summer Silver medals',
                    '4':'Summer Bronze medals',
                    '5':'Summer totals',
                    '6':'Winter games',
                    '7':'Winter Gold medals',
                    '8':'Winter Silver medals',
                    '9':'Winter Bronze medals',
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
        'Summer games':'int64',
        'Summer Gold medals':'int64',
        'Summer Silver medals':'int64',
        'Summer Bronze medals':'int64',
        'Summer totals':'int64',
        'Winter games':'int64',
        'Winter Gold medals':'int64',
        'Winter Silver medals':'int64',
        'Winter Bronze medals':'int64',
        'Winter totals':'int64',
        'Total games':'int64',
        'Gold':'int64',
        'Silver':'int64',
        'Bronze':'int64',
        'Total medals':'int64'        
        } 
    df = df.astype(type_mapping)
    return df 