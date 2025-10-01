import pandas as pd
from airflow.decorators import dag, task
from airflow.models import Variable
from datetime import datetime, timedelta
from extraction.extract import extract_from_csv
from extraction.transform import rename_columns, clean_columns, change_values, null_treatment, ranking_countries
from extraction.load import save_data_as_delta

@dag(
    dag_id="olympic_dag",
    start_date=datetime(2023, 1, 1),
    schedule="@monthly",
    catchup=False,
    tags=["olympics"],
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=3),
    }
)
def olympic_pipeline():

    @task()
    def _extract():
        raw_path = Variable.get("olympic_raw_path")
        bronze_path = Variable.get("bronze_path")
        df = extract_from_csv(raw_path)
        save_data_as_delta(df, bronze_path)
        return bronze_path
    
    @task()
    def _transform(bronze_path: str):
        silver_path = Variable.get("silver_path")
        df = pd.read_parquet(bronze_path)
        df = rename_columns(df)
        df = clean_columns(df)
        df = change_values(df)
        df = null_treatment(df)
        save_data_as_delta(df, silver_path)
        return silver_path
    
    @task()
    def _load(silver_path: str):
        gold_path = Variable.get("gold_path")
        df = pd.read_parquet(silver_path)
        df = ranking_countries(df)
        save_data_as_delta(df, gold_path)
        return gold_path
    
    bronze = _extract()
    silver = _transform(bronze)
    gold = _load(silver)
    
olympic_dag = olympic_pipeline
