import pyarrow as pa
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from deltalake import write_deltalake, DeltaTable
from extraction.extract import extract_from_csv
from extraction.transform import rename_columns, clean_columns, change_values, null_treatment, ranking_countries
from extraction.config import olympic_raw_path, bronze_path, silver_path, gold_path
from logger import get_logger

logger = get_logger(__name__)

def save_data_as_delta(df, path, mode="overwrite", partition_cols=None):
    write_deltalake(
        path, df, mode=mode, partition_by=partition_cols
        )

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
write_deltalake(bronze_path, df_bronze_olympic, mode="overwrite")

df_silver_olympic = rename_columns(df_bronze_olympic)
df_silver_olympic = clean_columns(df_silver_olympic)
df_silver_olympic = change_values(df_silver_olympic)
df_silver_olympic = null_treatment(df_silver_olympic)
write_deltalake(silver_path, df_silver_olympic, mode="overwrite")


df_gold_olympic = ranking_countries(df_silver_olympic)
write_deltalake(gold_path, df_gold_olympic, mode="overwrite")