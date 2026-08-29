# 🔄 ADF Orchestration Pipeline

This directory contains the Azure Data Factory (ADF) pipeline definition used to automate and orchestrate the end-to-end ETL execution.

---

## 📄 Files

- **`pl_transit_etl_orchestration.json`**: The exported ADF pipeline definition that sequentially triggers the Bronze-to-Silver, Silver-to-Gold, and Incremental Merge Databricks notebooks.

---

## 🚀 How to Use

1. Open **Azure Data Factory Studio**.
2. Go to **Authoring** > **Pipelines**.
3. Import `pl_transit_etl_orchestration.json` into your ADF instance.
4. Ensure your **Azure Databricks Linked Service** is properly configured.
5. Trigger or schedule the pipeline execution.
