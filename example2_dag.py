from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="example2_dag",
    description="Second test DAG",
    default_args=default_args,
    schedule=timedelta(days=1),  # ✅ new parameter name
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    t2 = BashOperator(
        task_id="say_hello",
        bash_command="echo 'Hello from Airflow!'",
    )

    t1 >> t2
