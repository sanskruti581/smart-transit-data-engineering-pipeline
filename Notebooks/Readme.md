
# 📓 Databricks Processing Notebooks

This directory contains the PySpark notebooks executed on Azure Databricks to transform and process telemetry data across the Medallion Architecture layers.

---

## 📄 Notebooks

- **`01_bronze_to_silver.ipynb`**: Cleans raw Bronze CSV/JSON data, performs schema enforcement, and writes standardized Delta tables.
- **`02_silver_to_gold.ipynb`**: Aggregates Silver Delta tables to compute business metrics and KPIs (route performance, bus utilization, daily revenue).
- **`03_incremental_trips_merge.ipynb`**: Handles daily incremental batch appends and upserts into Delta Lake.
