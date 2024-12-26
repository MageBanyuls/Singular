from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src import bronze_layer
from src import silver_layer
from src import gold_layer
from src import graphs


file_path = '/opt/airflow/data/transactions.csv'
load_bronze_data = bronze_layer.load_bronze_data
clean_silver_layer = silver_layer.clean_silver_layer
run_gold_layer_funcs = gold_layer.run_gold_layer_funcs
create_and_generate_report = graphs.create_and_generate_report





default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'transaction_pipeline',
    default_args=default_args,
    description='ETL pipeline for processing e-commerce data',
    schedule_interval='@monthly',
    start_date=datetime(year=2024, month=12, day=24),
    catchup=False,
    tags=['transaction', 'ETL'],
) as dag:

    # 1. Load raw data into bronze layer
    task_load_bronze = PythonOperator(
        task_id='load_bronze_data',
        python_callable=load_bronze_data,
        op_args=[file_path],
    )

    # 2. Clean data in the silver layer
    task_clean_silver = PythonOperator(
        task_id='clean_silver_data',
        python_callable=clean_silver_layer,
    )

    # 3. Execute the transformation and data analysis for the gold layer
    task_gold_layer = PythonOperator(
        task_id='run_gold_layer',
        python_callable=run_gold_layer_funcs,
    )

    # 4. Create report
    task_create_report = PythonOperator(
        task_id='create_report',
        python_callable=create_and_generate_report,
    )

    

    # Task dependencies
    task_load_bronze >> task_clean_silver
    task_clean_silver >> task_gold_layer
    task_gold_layer >> task_create_report
 