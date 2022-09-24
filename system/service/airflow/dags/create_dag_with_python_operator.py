from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def first_function(name, ti):
    first_name = ti.xcom_pull(task_ids = "task_3", key = "first_name")
    school = ti.xcom_pull(task_ids = "task_3", key = "school")
    text1 = f"hello world {first_name} and I comment {school}"
    print(text1)

def get_name():
    return "vua trai dat"

def get_info(ti):
    ti.xcom_push(key = "first_name", value = "CongDC")
    ti.xcom_push(key = "school", value = "HUST")

with DAG(
    dag_id='cap_nhap_hang_doi',
    default_args=default_args,
    description= "This is our second dag that we write",
    start_date=datetime(2022, 9, 5, 7),
    schedule_interval='@daily'
) as dag:
    
    task1 = PythonOperator(
        task_id = "task_1",
        python_callable = first_function,
        op_kwargs = {"name" : "cong"}
    )

    task2 = PythonOperator(
        task_id = "task_2",
        python_callable = get_name
    )
    
    
    task3 = PythonOperator(
        task_id = "task_3",
        python_callable = get_info
    )
    [task2, task3] >> task1