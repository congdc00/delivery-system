from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='first_dag_v14',
    default_args=default_args,
    description= "This is our first dag that we write",
    start_date=datetime(2022, 9, 5, 7),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo tao la Dinh chi cong!"
    )

    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = "echo Dm log nhu lon"
    )

    task3 = BashOperator(
        task_id = "third_task",
        bash_command = "echo Vai lon luon"
    )

    task1 >> [task2, task3]
