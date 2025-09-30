import pyarrow as pa
import sys, os
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from deltalake import write_deltalake, DeltaTable
from extraction.extract import extract_from_csv
from extraction.transform import rename_columns, clean_columns, change_values, null_treatment, ranking_countries
from extraction.config import olympic_raw_path, bronze_path, silver_path, gold_path
from logger import get_logger

logger = get_logger(__name__)

def save_data_as_delta(df: pd.DataFrame, path: str):
    try:
        if not isinstance(df, pd.DataFrame):
            df = pd.DataFrame(df)
        write_deltalake(path, df, mode = "overwrite")
        logger.info(f"Datos guardados en {path}")
    except Exception as e:
        logger.error(f"Error tipo {e}")
        raise

def save_new_data_as_delta(new_data, data_path, predicate, partition_cols=None):
    try:
        dt = DeltaTable(data_path)
        new_data_pa = pa.Table.from_pandas(new_data)
        dt.merge(
            source=new_data_pa,
            source_alias="source",
            target_alias="target",
            predicate=predicate
        ) \
        .when_not_matched_insert_all() \
        .execute()
    
    except TableNotFoundError:
        save_data_as_delta(new_data, data_path, partition_cols=partition_cols)
        
def upsert_data_as_delta(data, data_path, predicate):
    try:
        dt = DeltaTable(data_path)
        data_pa = pa.Table.from_pandas(data)
        dt.merge(
            source=data_pa,
            source_alias="source",
            target_alias="target",
            predicate=predicate
        ) \
        .when_matched_update_all() \
        .when_not_matched_insert_all() \
        .execute()
    except TableNotFoundError:
        save_data_as_delta(data, data_path)
        
def save_in_deltalake(df):
    write_deltalake(
        olympic_raw_path,
        mode="overwrite",
        schema_mode="merge",
        partition_by=[]
    )
    
    dt= DeltaTable(olympic_raw_path)
    logger.info("Cantidad de filas:", dt.to_pandas().shape[0])


df_bronze_olympic = extract_from_csv(olympic_raw_path)
table_bronze = pa.Table.from_pandas(df_bronze_olympic)
write_deltalake(bronze_path, table_bronze, mode="overwrite")

df_silver_olympic = rename_columns(df_bronze_olympic)
df_silver_olympic = clean_columns(df_silver_olympic)
df_silver_olympic = change_values(df_silver_olympic)
df_silver_olympic = null_treatment(df_silver_olympic)
silver_table = pa.Table.from_pandas(df_silver_olympic)
write_deltalake(silver_path, silver_table, mode="overwrite")


df_gold_olympic = ranking_countries(df_silver_olympic)
gold_table = pa.Table.from_pandas(df_gold_olympic)
write_deltalake(gold_path, gold_table, mode="overwrite")