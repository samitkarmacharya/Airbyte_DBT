# End-to-End Data Engineering Project

This repository contains an end-to-end data engineering project that demonstrates how to build a modern, production-style analytics pipeline using open-source and cloud-native tools.

The goal of this project is to show how raw, scattered data can be ingested, transformed, tested, and deployed into analytics-ready datasets using best practices commonly found in real-world data platforms.

---

## 🏗️ Architecture Overview

The project follows a modern ELT/lakehouse-style architecture:

- **Airbyte** for data ingestion
- **Databricks** for scalable data processing and storage
- **dbt** for transformations, testing, and documentation
- **GitHub Actions** for CI/CD and automated validation

Data flows through **bronze → silver → gold** layers and is modeled for downstream analytics and reporting use cases.

---

## 📦 Prerequisites

Before getting started, ensure the following tools are installed on your machine:

### 1. Python 3

Python 3 is required for local development and tooling.

- Download from: https://www.python.org/downloads/
- Verify installation:

```bash
python3 --version

```

### 2. Docker Desktop

Docker is required to run Airbyte locally.

- Download Docker Desktop for your OS:
  https://www.docker.com/products/docker-desktop/
- Verify installation:

```bash
docker --version
docker compose version
```

Make sure Docker Desktop is running before proceeding.

---

## 📁 Repository Structure

```text
.
├── airbyte/            # Airbyte configuration and connections
├── dbt/                # dbt project (models, tests, docs)
├── databricks/         # Databricks notebooks / jobs
├── .github/workflows/  # GitHub Actions (CI/CD)
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started


## 🐍 Python Virtual Environment

Create and activate a virtual environment:

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 🔌 Airbyte Installation (abctl)

Airbyte is installed locally using **abctl**.

### 1. Install abctl

```bash
curl -LsfS https://get.airbyte.com | bash
```

Verify installation:

```bash
abctl version
```

### 2. Start Airbyte

```bash
abctl local install
```

Airbyte UI will be available at:
```
http://localhost:8000
```

Use the UI to:
- Configure source connectors
- Configure destination (lakehouse / object storage)
- Create and run syncs

---

## 🔁 dbt Setup (Databricks)

### 1. Install dbt for Databricks

```bash
pip install dbt-databricks
```

Verify installation:

```bash
dbt --version
```

### 2. dbt Profiles Configuration

Create a `profiles.yml` file:

```yaml
dbt_transformation:
  outputs:
    dev:
      catalog: "{{env_var('DATABRICKS_CATALOG', '')}}"
      host: 
      http_path: /
      schema: 
      threads: 1
      token: 
      type: databricks
  target: dev
```


### 3. Run dbt

```bash
dbt debug
dbt run
dbt test
dbt docs generate
dbt docs serve
```

---

## ⚙️ CI/CD with GitHub Actions

This project uses **GitHub Actions** to automate validation and deployment workflows.

Typical CI steps include:
- Installing dependencies
- Running `dbt debug`, `dbt run`, and `dbt test`
- Failing fast on data quality or schema issues

Example workflow snippet:

```yaml
- name: Run dbt
  run: |
    dbt deps
    dbt run
    dbt test
    dbt build
```
---

---

## Airflow (Local)

Airflow is included to orchestrate the dbt transformation workflow.

```bash
cd airflow
docker compose up -d
```

Open `http://localhost:8080` and log in with `admin` / `admin`.

The default DAG is `dbt_daily`, which runs `dbt deps`, `dbt run`, and `dbt test`.
