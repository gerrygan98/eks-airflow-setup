from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'example_kubernetes_executor',
    default_args=default_args,
    description='A simple DAG using KubernetesExecutor',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

# Define the task
print_date = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

# Set the task dependencies
print_date
