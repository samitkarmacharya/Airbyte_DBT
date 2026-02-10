# Airflow

This folder adds a local Airflow setup that runs the dbt project on a schedule.

## Run Airflow (SQLite)

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

## Run Airflow (Postgres-backed)

This is recommended beyond local dev to avoid SQLite limitations.

```bash
docker compose -f docker-compose.postgres.yaml up -d
```

The Postgres settings are in `airflow/.env`:

- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`

## DAGs

- `dbt_daily`: runs `dbt deps`, `dbt run`, `dbt test` against the project at `../dbt_transformation`.
