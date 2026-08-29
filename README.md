# 🚌 Smart Transit Data Engineering Pipeline

An end-to-end **Azure-based data engineering lakehouse pipeline** built using **Azure Data Lake Storage Gen2 (ADLS Gen2), Azure Databricks, PySpark, Delta Lake, and Azure Data Factory (ADF)**.

The project simulates a real-world public transit data platform that ingests synthetic telemetry from buses, routes, trips, passengers, payments, and vehicle events. The data is processed through a **Medallion Architecture (Bronze → Silver → Gold)** to produce operational analytics and business KPIs.

---

## 📌 Project Overview

The **Smart Transit Data Engineering Pipeline** demonstrates how raw transportation data can be ingested, cleaned, transformed, incrementally processed, and converted into business-ready analytics.

### Key Objectives

* Ingest multi-source transit data into **ADLS Gen2**
* Process raw data using **Azure Databricks and PySpark**
* Implement **Bronze, Silver, and Gold** data layers
* Store processed data using **Delta Lake**
* Perform data cleansing, type enforcement, and deduplication
* Implement **incremental batch processing**
* Generate operational and financial KPIs
* Orchestrate the complete workflow using **Azure Data Factory**

---

# 🏗️ Architecture

```text
                    ┌─────────────────────────────┐
                    │ Synthetic Telemetry Generator│
                    │       Python / Pandas        │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │      ADLS Gen2 - Bronze     │
                    │      Raw CSV / JSON Data     │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │     Azure Databricks         │
                    │       PySpark Processing     │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │       ADLS Gen2 - Silver    │
                    │   Cleaned Delta Tables      │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │   Business Transformations  │
                    │      & KPI Aggregations     │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │        ADLS Gen2 - Gold     │
                    │   Analytical Delta Tables   │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │    Azure Data Factory       │
                    │       Orchestration         │
                    └─────────────────────────────┘
```

---

# 🧰 Technology Stack

| Technology                       | Purpose                           |
| -------------------------------- | --------------------------------- |
| **Azure Data Lake Storage Gen2** | Cloud data storage                |
| **Azure Databricks**             | Distributed data processing       |
| **PySpark**                      | Data cleansing and transformation |
| **Delta Lake**                   | Reliable analytical data storage  |
| **Azure Data Factory**           | Pipeline orchestration            |
| **Python**                       | Synthetic data generation         |
| **SQL**                          | Data analysis and transformations |
| **CSV / JSON**                   | Raw source data formats           |

---

# 🏔️ Medallion Architecture

The pipeline follows the standard **Medallion Architecture**:

```text
             RAW DATA
                 │
                 ▼
        ┌─────────────────┐
        │     BRONZE      │
        │ Raw CSV / JSON  │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │     SILVER      │
        │ Cleaned + Typed │
        │ Deduplicated    │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │      GOLD       │
        │ Business KPIs   │
        │ Analytics       │
        └─────────────────┘
```

## 🥉 1. Bronze Layer — Raw Ingestion

The Bronze layer stores raw data received from different transit data sources.

### Input Datasets

| File                  | Description                                                |
| --------------------- | ---------------------------------------------------------- |
| `buses.csv`           | Bus metadata including capacity, status, and plate numbers |
| `routes.csv`          | Transit route information and base fares                   |
| `passengers.csv`      | Passenger demographic and card information                 |
| `trips_01.csv`        | Initial operational trip records                           |
| `trips_02.csv`        | Incremental trip records                                   |
| `payments.csv`        | Payment transactions and payment methods                   |
| `vehicle_events.json` | Vehicle warnings, door activity, and engine events         |

The Bronze layer preserves the source data with minimal transformation.

---

# 🥈 2. Silver Layer — Cleansing & Standardization

The Silver layer converts raw data into clean and structured Delta tables.

### Transformations

* Convert columns to appropriate data types
* Cast strings into:

  * Integer
  * Double
  * Timestamp
* Remove duplicate records
* Enforce entity uniqueness
* Handle inconsistent source values
* Add ingestion metadata
* Convert raw files into **Delta format**

### Example Metadata

```text
ingested_at
```

This timestamp provides basic auditability and helps identify when records entered the pipeline.

### Deduplication Examples

```text
trip_id
payment_id
bus_id
```

Duplicate records are removed before data reaches the Gold layer.

---

# 🥇 3. Gold Layer — Business Analytics

The Gold layer contains business-ready datasets generated from the cleaned Silver data.

## 📊 Gold Route Performance

### Table

```text
gold_route_performance
```

Provides route-level operational and financial metrics.

### Metrics

* Total revenue
* Number of trips
* Total passengers
* Average passengers per trip
* Route-level performance

Example structure:

```text
route_id
route_name
total_trips
total_passengers
total_revenue
avg_passengers_per_trip
```

---

## 🚌 Gold Bus Utilization

### Table

```text
gold_bus_utilization
```

Measures how effectively each bus's available passenger capacity is being utilized.

### Metrics

* Bus capacity
* Passenger count
* Capacity utilization percentage

Conceptually:

```text
Capacity Utilization %
=
Total Passengers / Available Capacity × 100
```

This can help identify buses that are consistently underutilized or heavily utilized.

---

## 💰 Gold Daily Revenue

### Table

```text
gold_daily_revenue
```

Provides daily revenue trends grouped by payment channel.

### Payment Channels

Examples include:

```text
SmartCard
Cash
MobileApp
```

### Example Structure

```text
date
payment_method
transaction_count
total_revenue
```

This dataset can be used to analyze revenue trends and payment-channel performance.

---

# 🔄 Incremental Batch Processing

The project also demonstrates **incremental data processing**.

Instead of reprocessing the complete historical dataset, a second batch of trip data is introduced through:

```text
trips_02.csv
```

The incremental workflow processes only the newly arrived data and appends or merges it into the existing Delta-based dataset.

```text
Day 1
trips_01.csv
     │
     ▼
Silver Delta
     │
     ▼
Gold KPIs


Day 2
trips_02.csv
     │
     ▼
Incremental Processing
     │
     ▼
Updated Silver Delta
     │
     ▼
Updated Gold KPIs
```

This simulates how a production data pipeline can process continuously arriving operational data without unnecessarily reloading the entire historical dataset.

---

# 📁 Repository Structure

```text
smart-transit-data-engineering-pipeline/
│
├── data/
│   └── generate_synthetic_data.py
│       # Generates synthetic transit telemetry
│
├── notebooks/
│   ├── 01_bronze_to_silver.py
│   │   # Bronze → Silver processing
│   │
│   ├── 02_silver_to_gold.py
│   │   # Silver → Gold KPI aggregation
│   │
│   └── 03_incremental_trips_merge.py
│       # Incremental batch processing
│
├── adf/
│   ├── pipeline/
│   │   └── pl_transit_etl_orchestration.json
│   │       # ADF orchestration pipeline
│   │
│   └── linkedService/
│       └── ls_azure_databricks.json
│           # Databricks linked service
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 🚀 Getting Started

## Prerequisites

Before running the project, ensure you have:

* Azure Subscription
* ADLS Gen2 Storage Account
* Azure Databricks Workspace
* Azure Data Factory
* Python 3.8+
* Pandas

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/sanskruti581/smart-transit-data-engineering-pipeline.git
cd smart-transit-data-engineering-pipeline
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Generate Synthetic Data

Run the data-generation script:

```bash
python data/generate_synthetic_data.py
```

This generates the synthetic transit datasets used by the pipeline.

---

## 4️⃣ Upload Data to ADLS Gen2

Upload the generated files into the **Bronze container** of your ADLS Gen2 storage account.

Example:

```text
ADLS Gen2
│
└── bronze/
    ├── buses.csv
    ├── routes.csv
    ├── passengers.csv
    ├── trips_01.csv
    ├── trips_02.csv
    ├── payments.csv
    └── vehicle_events.json
```

---

# ⚡ Running the Databricks Pipeline

## Step 1 — Bronze → Silver

Run:

```text
notebooks/01_bronze_to_silver.py
```

This performs:

```text
Raw CSV / JSON
      ↓
Data Type Conversion
      ↓
Deduplication
      ↓
Data Standardization
      ↓
Add ingested_at
      ↓
Silver Delta Tables
```

---

## Step 2 — Silver → Gold

Run:

```text
notebooks/02_silver_to_gold.py
```

This generates:

```text
gold_route_performance
gold_bus_utilization
gold_daily_revenue
```

---

## Step 3 — Incremental Processing

Run:

```text
notebooks/03_incremental_trips_merge.py
```

This processes the second trip batch:

```text
trips_02.csv
```

and updates the existing Delta-based data without requiring a complete historical reload.

---

# 🔄 Azure Data Factory Orchestration

The ADF pipeline coordinates the end-to-end workflow.

```text
             ADF Pipeline
                  │
                  ▼
       ┌─────────────────────┐
       │ Bronze Data Available│
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ Bronze → Silver      │
       │ Databricks Notebook  │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ Silver → Gold        │
       │ Databricks Notebook  │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ Incremental Load     │
       │ Databricks Notebook  │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ Pipeline Completed   │
       └─────────────────────┘
```

The exported ADF configuration is available under:

```text
adf/pipeline/
```

and the Databricks linked service definition is available under:

```text
adf/linkedService/
```

---

# 📈 Key Business KPIs

The pipeline produces several operational metrics:

| KPI                         | Description                                   |
| --------------------------- | --------------------------------------------- |
| **Total Revenue**           | Revenue generated from transit payments       |
| **Trip Volume**             | Number of trips operated                      |
| **Passenger Count**         | Total passengers served                       |
| **Average Passengers/Trip** | Average passengers carried per trip           |
| **Bus Utilization**         | Percentage of available bus capacity utilized |
| **Daily Revenue**           | Revenue generated per day                     |
| **Payment Channel Revenue** | Revenue grouped by payment method             |

---

# 🔐 Data Engineering Concepts Demonstrated

This project demonstrates several concepts commonly used in modern data engineering:

* **ETL Pipeline**
* **Cloud Data Lake**
* **Medallion Architecture**
* **Batch Processing**
* **Incremental Data Processing**
* **Data Cleansing**
* **Data Type Enforcement**
* **Deduplication**
* **Distributed Processing**
* **PySpark DataFrames**
* **Delta Lake**
* **Data Aggregation**
* **KPI Generation**
* **Pipeline Orchestration**
* **ADLS Gen2**
* **Azure Databricks**
* **Azure Data Factory**

---

# 🎯 Project Workflow

The complete data flow can be summarized as:

```text
Synthetic Data
      │
      ▼
   ADLS Gen2
   ┌───────┐
   │Bronze │
   └───┬───┘
       │
       ▼
 Azure Databricks
    PySpark
       │
       ▼
   ┌───────┐
   │Silver │
   │ Delta │
   └───┬───┘
       │
       ▼
 Business Transformations
       │
       ▼
   ┌───────┐
   │ Gold  │
   │ Delta │
   └───┬───┘
       │
       ▼
 Operational Analytics
       │
       ▼
 Azure Data Factory
   Orchestration
```

---

# 💡 Why This Project?

Public transportation systems generate large volumes of operational and transactional data. A scalable data platform is required to transform this raw data into reliable information for operational decision-making.

This project demonstrates how a modern cloud data engineering architecture can be used to:

* Monitor transit operations
* Analyze route performance
* Measure fleet utilization
* Track revenue
* Analyze payment channels
* Process incremental data efficiently

---

# 👩‍💻 Author

**Sanskruti Shinde**

B.Tech Computer Engineering

### Areas of Interest

* Data Engineering
* Cloud Computing
* PySpark
* Azure
* Big Data
* Full-Stack Development

