# 📊 Synthetic Telemetry Datasets & Generation

This directory contains the synthetic data generation script along with the raw CSV telemetry datasets used for initial Bronze layer ingestion into ADLS Gen2.

---

## 📄 Contents

- **`generate_synthetic_data.py`**: Python script to generate synthetic transit telemetry files.
- **`buses.csv`**: Bus fleet metadata (capacity, status, plate numbers).
- **`routes.csv`**: Transit route details and base fares.
- **`passengers.csv`**: Demographics and pass types.
- **`payments.csv`**: Fare collection transactions.
- **`trips_01.csv` & `trips_02.csv`**: Historical and incremental operational trip logs.
