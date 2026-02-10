# Airflow

This folder adds a local Airflow setup that runs the dbt project on a schedule.

## Run Airflow

From this folder:

```bash
docker compose up -d
```

Open the UI at:

```
http://localhost:8080
```

Login:
- Username: admin
- Password: admin

## DAGs

- `dbt_daily`: runs `dbt deps`, `dbt run`, `dbt test` against the project at `../dbt_transformation`.
