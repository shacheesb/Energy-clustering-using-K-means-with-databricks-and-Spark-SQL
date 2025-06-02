# 🔌 Energy Usage Clustering and Forecasting

This project analyzes hourly household energy consumption data to uncover usage patterns using unsupervised clustering and forecast future consumption using linear regression. Built with PySpark, Spark SQL, and scikit-learn, the project demonstrates how data science can uncover actionable insights in energy behavior.

---

## 📊 Project Overview

- **Clustering**: Used PySpark and Spark MLlib to group hourly usage patterns across 24-hour cycles using k-means.
- **Forecasting**: Applied linear regression (scikit-learn) to model and predict average power usage across hours.
- **Visualization**: Created clear plots comparing actual vs. predicted usage using Seaborn and Matplotlib.
- **Deployment-Ready**: The workflow runs smoothly on Databricks or Jupyter, with CSV export support.

---

## 📁 Files

| File | Description |
|------|-------------|
| `Energy Usage Clustering and Forecasting Web App.ipynb` | Main notebook with clustering, regression, plots, and export |
| `hourly_clusters.csv` | Cleaned data with hourly usage and cluster labels |
| `clustered_with_forecast.csv` | Output with added forecast column |
| `hourly_forecast_plot.png` | Plot showing actual vs forecasted power usage |

---

## 🛠️ Tech Stack

- **Python**, **Pandas**, **Matplotlib**, **Seaborn**
- **PySpark**, **Spark SQL**, **Spark MLlib**
- **scikit-learn** for regression
- **Databricks** for distributed data processing and clustering
- **Streamlit** for dashboard UI

---

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/energy-forecasting.git
   cd energy-forecasting
   ```

2. Open the Jupyter notebook:
   - In Databricks

3. Run cells in order:
   - Data loading
   - Cleaning
   - Clustering
   - Forecasting
   - Visualization

4.  Run the Streamlit version:
   ```bash
   streamlit run app.py
   ```



## ✨ Future Work

- Integrate temperature/weather features
- Try Prophet or LSTM for time-series forecasting
- Deploy as a public Streamlit dashboard
- Add anomaly detection during peak load times





