import pyarrow as pa
import pandas as pd
from deltalake import write_deltalake, DeltaTable 
from logger import get_logger

logger = get_logger(__name__)

def save_data_as_delta(df, path: str, mode="overwrite"):
    write_deltalake(
        path, df, mode=mode
    )

def save_new_data_as_delta(new_data, data_path, predicate):
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
        save_data_as_delta(new_data, data_path)

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
    
