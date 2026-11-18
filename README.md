# Data Science Zero to Hero on AWS & Azure Practice

Hands-on repository for the **Data Science Zero to Hero on AWS & Azure** course. This repository tracks daily milestones across the data science lifecycle, culminating in the **CityPulse** production forecasting system.

---

## 📁 Repository Structure

All code and deliverables are organized strictly within their milestone folders. The root directory contains only shared environment configuration, dependency definitions, and project documentation:

```text
data-science-practice/
├── .env                  # Cloud secrets, AWS/Azure credentials (Never committed)
├── .env.example          # Sanitized configuration template
├── .gitignore            # Excludes datasets, model artifacts, caches, and secrets
├── config.py             # Central project configuration & directory resolution
├── pyproject.toml        # Pinned data stack dependencies managed via uv
├── day1_foundations/     # Milestone 1: Data Foundations, Statistics & Exploratory Data Analysis
├── day2_langchain/       # Milestone 2: Feature Engineering, Data Validation & Ingestion
├── day3_langgraph/       # Milestone 3: Model Training, Optuna Tuning & MLflow Registry
├── day4_adk/             # Milestone 4: Serving (FastAPI/Streamlit) & Drift Monitoring
├── day5_observability/   # Observability, Cloud Pipelines (SageMaker/Azure ML) & CI/CD
├── capstone/             # CityPulse: Production NYC Taxi Forecasting System
├── data/                 # Local Parquet storage & DuckDB database files
├── evals/                # Test suites, Pandera schemas & validation benchmarks
└── notes/                # Architecture Decision Records (ADRs) & cost tracking logs
```

---

## ⚙️ Central Configuration (`config.py`)

All scripts import configuration from the root `config.py`:
* **Path Resolution**: Provides resolved paths to the `data/` directory and project root.
* **Environment Loading**: Automatically loads `.env` across local scripts, Jupyter notebooks, and test runners.
* **Cloud Profiles**: Sets default regions and profiles for AWS (`us-east-1`) and Azure (`eastus`).

---

## 🚀 Getting Started

### 1. Environment Setup

Ensure Python 3.12 is active and install the course dependencies using `uv`:

```powershell
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install course pinned dependencies
uv sync
```

### 2. Configure Credentials

Copy `.env.example` to `.env` and fill in your cloud parameters:

```ini
# AWS Configuration (us-east-1 for NYC taxi datasets)
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
SAGEMAKER_ROLE_ARN=arn:aws:iam::...

# Azure Configuration
AZURE_SUBSCRIPTION_ID=your_sub_id
AZURE_RESOURCE_GROUP=rg-ds-course
AZURE_LOCATION=eastus

# Tracking & Storage
MLFLOW_TRACKING_URI=http://localhost:5000
DATA_DIR=./data
```

---

## 📚 Core Milestones & Deliverables

| Milestone | Directory | Focus & Deliverables |
| :--- | :--- | :--- |
| **Milestone 1: Data Foundations** | `day1_foundations/` | • Ingestion & profiling of NYC TLC Yellow Taxi Parquet files.<br>• Performance benchmark comparing Pandas, Polars, and DuckDB.<br>• Statistical distribution and outlier detection analysis. |
| **Milestone 2: Feature Engineering** | `day2_langchain/` | • Reusable feature pipelines using Scikit-Learn and Polars.<br>• Data validation contracts using Pandera / Great Expectations.<br>• Local dbt transformations with `dbt-duckdb`. |
| **Milestone 3: Training & Tuning** | `day3_langgraph/` | • Baseline regression models (Ridge, Random Forest, LightGBM, XGBoost).<br>• Hyperparameter optimization using Optuna.<br>• Experiment tracking and model registration with MLflow.<br>• SHAP feature importance analysis. |
| **Milestone 4: Serving & Monitoring** | `day4_adk/` | • Real-time inference REST API built with FastAPI.<br>• Interactive forecasting dashboard built with Streamlit.<br>• Data drift and prediction drift reports with Evidently. |
| **Milestone 5: Cloud & MLOps** | `day5_observability/` | • SageMaker training job / Azure ML command job orchestration.<br>• Prefect workflow scheduling for daily retraining.<br>• Automated testing and GitHub Actions CI workflow. |
| **Capstone: CityPulse** | `capstone/` | • End-to-end taxi demand and duration forecasting system combining dbt, MLflow, serverless inference, and automated teardown. |

---

## 🛡️ Cost Guardrails & Teardown Protocol

1. **Zero-Spend Budgets**: Always set a zero-spend or \$5 limit alert in both AWS Billing and Azure Cost Management.
2. **Ephemeral Compute**: Never leave real-time endpoints or notebook instances running. Deploy, test, and delete in the same session.
3. **Daily Teardown**: Run cloud teardown commands at the end of every practice session:

```powershell
# Delete SageMaker endpoints (AWS)
aws sagemaker list-endpoints --query "Endpoints[].EndpointName" --output text
aws sagemaker delete-endpoint --endpoint-name <endpoint-name>

# Stop Azure ML compute instances (Azure)
az ml compute stop -n <compute-instance> -g rg-ds-course -w <workspace>
```
