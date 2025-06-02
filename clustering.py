import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Energy Usage Clustering", layout="wide")
st.title("🔌 Energy Usage Clustering Dashboard")

# Upload or load local CSV
uploaded_file = st.file_uploader("/Users/shacheesb/Downloads/energy_clustering_data.csv", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()
    st.write("✅ Cleaned columns:", list(df.columns))

    st.markdown("### 📊 Raw Data")
    st.dataframe(df)

    st.markdown("### 📈 Hourly Energy Usage by Cluster")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df, x="hour", y="avg_power", hue="prediction", palette="tab10", marker="o", ax=ax)
    plt.xlabel("Hour of Day")
    plt.ylabel("Average Power (kW)")
    plt.title("Clustered Hourly Power Usage Patterns")
    st.pyplot(fig)

    st.markdown("### 🔍 Explore Cluster Details")
    selected_cluster = st.selectbox("Select a Cluster:", sorted(df['prediction'].unique()))
    cluster_df = df[df['prediction'] == selected_cluster]
    st.write(f"Showing hours assigned to Cluster {selected_cluster}:")
    st.table(cluster_df.sort_values(by="hour"))

    st.markdown("### 📊 Cluster Size Distribution")
    st.bar_chart(df["prediction"].value_counts().sort_index())


else:
    st.info("Please upload the clustered CSV file to begin.")
