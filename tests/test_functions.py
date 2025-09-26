import pandas as pd
import numpy as np
from extraction.transform import rename_columns, clean_columns, change_values, null_treatment, ranking_countries
from extraction.load import df_bronze_olympic

def test_rename_columns():
    df = rename_columns(df_bronze_olympic.copy())
    assert "Paises" in df.columns

def test_clean_columns():
    df = rename_columns(df_bronze_olympic.copy())
    df = clean_columns(df)
    assert 0 not in df.index

def test_change_values():
    df = rename_columns(df_bronze_olympic.copy())
    df = clean_columns(df)
    df = change_values(df)
    assert pd.api.types.is_integer_dtype(df["Summer games"])

def test_null_treatment():
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
    df = rename_columns(df_bronze_olympic.copy())
    df = clean_columns(df)
    df = ranking_countries(df)
    assert "Total medals" in df.columns

