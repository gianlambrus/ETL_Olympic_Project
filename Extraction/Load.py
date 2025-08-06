import os
import pandas as pd
import pyarrow as pa 
from deltalake import write_deltalake, DeltaTable
from deltalake.exceptions import TableNotFoundError
from deltalake.table import TableOptimizer
from Extract import extract_from_csv
from Transform import rename_columns, clean_columns, change_values, df_bronze_olympic, df_silver_olympic
from Config import bronze_path, silver_path

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
        olympic_raw_dir,
        olympic_df,
        mode="overwrite",
        schema_mode="merge",
        partition_by=[]
    )
    
    dt= DeltaTable(olympic_raw_dir)
    print("Cantidad de filas:", dt.to_pandas().shape[0])

bronze_path = save_data_as_delta(df_bronze_olympic, bronze_path)
silver_path = save_data_as_delta(df_silver_olympic, silver_path)
