from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Default arguments applied to all tasks
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

# Define the DAG
with DAG(
    dag_id='example_test_dag',
    default_args=default_args,
    description='A simple test DAG to verify Airflow setup',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['test'],
) as dag:

    # Task 1 - Print date
    print_date = BashOperator(
        task_id='print_date',
        bash_command='date'
    )

    # Task 2 - Sleep for 5 seconds
    sleep_task = BashOperator(
        task_id='sleep_5s',
        bash_command='sleep 5'
    )

    # Task 3 - Echo a templated variable
    templated = BashOperator(
        task_id='templated_task',
        bash_command="""
        echo "Execution date is {{ ds }}"
        echo "Next execution date is {{ macros.ds_add(ds, 1) }}"
        """
    )

    # Define task dependencies
    print_date >> sleep_task >> templated
