from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 4, 8),
    'retries': 1,
}

with DAG('etl_dag',default_args=default_args,schedule_interval='@daily', template_searchpath=['/opt/airflow/sql_files'], catchup=True) as dag:
    create = PostgresOperator(
    task_id='create_table',
    postgres_conn_id='postgres',
    sql= 'create_table.sql',)

    insert = PostgresOperator(
    task_id='insert_into_table',
    postgres_conn_id='postgres',
    sql= 'insert_values.sql',)

    


    create >> insert 
