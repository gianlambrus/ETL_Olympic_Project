import pandas as pd

def rename_columns(df):
    #ES: Cambia el nombre de las columnas
    #EN: Change the name of the columns
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
    df=df.rename(columns=rename_mapping)
    return df


def clean_columns(df):
    #ES: Borra el indice 0 del DataFrame
    #EN: Drops the index 0 from the DataFrame
    df=df.drop(index=0)
    return df


def change_values(df):
    #ES: Cambia el valor de las columnas
    #EN: Change the value from the columns
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
    df=df.astype(type_mapping)
    return df

def null_treatment(df):
    #ES: Si encuentra valores nulos, los rellena con 0
    #EN: If it finds any null value, it change it to 0
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col]=df[col].replace([None], pd.NA).fillna(0)
    return df

def ranking_countries(df):
    #ES: Muestra el ranking de paises segun la cantidad total de medallas
    #EN: Shows the ranking of countries from the total medals
    df['ranking']=df['Total medals'].rank(ascending=False,method='dense')
    return df
