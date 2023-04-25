from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 11),
}

# Define the DAG
dag = DAG(
    'snowflake',
    default_args=default_args,
    description='A simple DAG that extracts data from one Snowflake table and loads it into another',
    schedule_interval=None,
)

# Define the extract function
def extract_data():
    # Use the SnowflakeOperator to extract data from a Snowflake table
    with SnowflakeOperator(
        task_id='extract_data',
        snowflake_conn_id='snowflake_connection',
        sql='SELECT * FROM EMPLOYEES',
        database='MYDB',
        warehouse='COMPUTE_WH',
    ) as extract_task:
        pass

# Define the load function
def load_data():
    # Use the SnowflakeOperator to load data into a Snowflake table
    with SnowflakeOperator(
        task_id='load_data',
        snowflake_conn_id='snowflake_connection',
        sql='INSERT INTO EMPLOYEES2 SELECT * FROM EMPLOYEES',
        database='MYDB',
        warehouse='COMPUTE_WH',
    ) as load_task:
        pass

# Define the tasks
extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_task',
    python_callable=load_data,
    dag=dag,
)

# Define the task dependencies
extract_task >> load_task
