# 🔋 Energy Usage Clustering and Forecasting with PySpark & Prophet

This project analyzes household power consumption data to uncover patterns and forecast future usage. It combines the scalability of Apache Spark with the interpretability of Prophet to deliver both **unsupervised clustering** and **time series forecasting** for energy usage.

---

## Project Highlights

### Clustering with K-Means (Spark MLlib)
- Grouped hourly usage patterns across the day.
- Identified behavioral clusters like peak/off-peak energy consumption.
- Used PySpark DataFrames and MLlib for scalable processing.

### Forecasting with Prophet
- Created accurate time series forecasts of `Global_active_power`.
- Visualized trend and uncertainty intervals.
- Used hourly data, downsampled to improve Prophet performance.

---

## Tech Stack

- **Apache Spark** (PySpark, Spark SQL, MLlib)
- **Prophet** for forecasting
- **Pandas**, **Matplotlib**, **Seaborn**
- **Databricks** (Cloud-based notebook environment)

---

## 📁 Notebooks & Outputs

| File | Description |
|------|-------------|
| `Energy Usage Clustering and Forecasting Web App.ipynb` | Spark-based clustering and export pipeline |
| `Prophet Time Series Forecasting.ipynb` | Prophet-based forecasting from cleaned Spark data |

---

## How to Run

### In Databricks
1. Upload your dataset (e.g., `household_power_consumption.txt`) to `dbfs:/FileStore/tables/`.
2. Attach notebook to a running cluster (Standard is fine).
3. Run cells in order:
   - Load and clean data with PySpark
   - Perform clustering with MLlib
   - Export to Pandas for Prophet
   - Forecast & visualize future usage

### Optional (Local)
```bash
pip install pandas matplotlib seaborn prophet
```

