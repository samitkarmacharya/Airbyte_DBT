import os

import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

DBT_PROJECT_DIR = os.getenv("DBT_PROJECT_DIR", "/opt/airflow/project/dbt_transformation")
DBT_PROFILES_DIR = os.getenv(
    "DBT_PROFILES_DIR",
    os.path.join(DBT_PROJECT_DIR, "config"),
)

with DAG(
    dag_id="dbt_daily",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    tags=["dbt"],
) as dag:
    dbt_deps = BashOperator(
        task_id="dbt_deps",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt deps",
        env={"DBT_PROFILES_DIR": DBT_PROFILES_DIR},
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt run",
        env={"DBT_PROFILES_DIR": DBT_PROFILES_DIR},
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_PROJECT_DIR} && dbt test",
        env={"DBT_PROFILES_DIR": DBT_PROFILES_DIR},
    )

    dbt_deps >> dbt_run >> dbt_test
