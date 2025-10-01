import pandas as pd
from extraction.transform import rename_columns, clean_columns, change_values, null_treatment, ranking_countries
from extraction.load import df_bronze_olympic

def test_rename_columns():
    #ES: Comprueba que se aplique el cambio de nombre de las columnas 
    #EN: Test the change of names applied to the columns
    df = rename_columns(df_bronze_olympic.copy())
    assert "Paises" in df.columns

def test_clean_columns():
    #ES: Comprueba que se aplique la baja del indice 0
    #EN: Test if the index drops when the function is invocated
    df = rename_columns(df_bronze_olympic.copy())
    df = clean_columns(df)
    assert 0 not in df.index

def test_change_values():
    #ES: Comprueba que se aplique el cambio de valores de las columnas
    #EN: Test the change of values applied to the columns
    df = rename_columns(df_bronze_olympic.copy())
    df = clean_columns(df)
    df = change_values(df)
    assert pd.api.types.is_integer_dtype(df["Summer games"])

def test_null_treatment():
    #ES: Comprueba que se aplique el tratamiento de valores nulos en las filas
    #EN: Test the null treatment applied to the rows
    df = rename_columns(df_bronze_olympic.copy())
    df = clean_columns(df)
    df["Gold"] = pd.to_numeric(df["Gold"], errors="coerce")
    df["Silver"] = pd.to_numeric(df["Silver"], errors="coerce")
    df["Bronze"] = pd.to_numeric(df["Bronze"], errors="coerce")
    df = null_treatment(df)
    assert df["Gold"].isna().sum() == 0
    assert df["Silver"].isna().sum() == 0
    assert df["Bronze"].isna().sum() == 0

def test_ranking_countries():
    #ES: Comprueba que se realice el ranking de los paises
    #EN: Test that the ranking shows correctly
    df = rename_columns(df_bronze_olympic.copy())
    df = clean_columns(df)
    df = ranking_countries(df)
    assert "Total medals" in df.columns

