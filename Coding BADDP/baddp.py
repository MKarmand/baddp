import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset
data_df = pd.read_csv("PRSA_Data_Changping_20130301-20170228.csv")

# Konversi tanggal
data_df['date'] = pd.to_datetime(data_df[['year', 'month', 'day', 'hour']])
data_df.set_index('date', inplace=True)

# Kategorisasi PM2.5
bins = [0, 50, 100, 150, 200, 300, 500]
labels = ['Baik', 'Sedang', 'Tidak Sehat', 'Sangat Tidak Sehat', 'Berbahaya', 'Sangat Berbahaya']
data_df['PM2.5_Category'] = pd.cut(data_df['PM2.5'], bins=bins, labels=labels, include_lowest=True)

st.title("Dashboard Tren Suhu dan PM2.5")

# Tren Suhu Bulanan
st.subheader("Tren Suhu Bulanan")
fig, ax = plt.subplots(figsize=(12, 5))
data_df['TEMP'].resample('M').mean().plot(marker='o', linestyle='-', color='r', ax=ax)
ax.set_title("Tren Suhu Bulanan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Suhu Rata-rata (°C)")
ax.grid(True)
st.pyplot(fig)

# Tren PM2.5 Bulanan
st.subheader("Tren PM2.5 Bulanan")
fig, ax = plt.subplots(figsize=(12, 5))
data_df['PM2.5'].resample('M').mean().plot(marker='o', linestyle='-', color='b', ax=ax)
ax.set_title("Tren PM2.5 Bulanan")
ax.set_xlabel("Bulan")
ax.set_ylabel("PM2.5 Rata-rata")
ax.grid(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
st.pyplot(fig)

# Visualisasi Kategori PM2.5
st.subheader("Kategori Kualitas Udara Berdasarkan PM2.5")
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(x=data_df['PM2.5_Category'], palette='coolwarm', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_title("Kategori Kualitas Udara Berdasarkan PM2.5")
st.pyplot(fig)

st.write("Dashboard ini menampilkan tren bulanan suhu rata-rata dan PM2.5 di Changping serta kategori kualitas udara berdasarkan PM2.5.")