from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="my_etl_dag",
    start_date=datetime(2026, 1, 1),
    schedule="10 6 * * *",
    catchup=False,
    tags=["demo", "bash"],
) as dag:

    # Start Task
    start = EmptyOperator(
        task_id="start"
    )

    # Bash Task - Execute Shell Script
    extract = BashOperator(
        task_id="Extract",
        bash_command="/home/azureuser/ethans-1124/extract.sh "
    )

    transform = BashOperator(
        task_id="Transform",
        bash_command="/home/azureuser/ethans-1124/etl.sh transform"
    )

    load = BashOperator(
        task_id="Load",
        bash_command="/home/azureuser/ethans-1124/etl.sh load"
    )

    # End Task
    end = EmptyOperator(
        task_id="end"
    )

    # Task Dependency using Shift Operator
    start >> extract >> transform >> load >> end