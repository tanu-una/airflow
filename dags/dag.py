from airflow import DAG
from airflow.operators.bash import BashOperator
from pendulum import datetime

with DAG(
    dag_id="example_airflow_3_dag",
    start_date=datetime(2024, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    tags=["example"],
) as dag:

    hello = BashOperator(
        task_id="hello_world",
        bash_command="echo 'Hello from Airflow 3.1.5'",
    )
