import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
day_url = "https://raw.githubusercontent.com/Sholahuddinoob/Bike-Sharing-Dataset/main/data/day.csv"
hour_url = "https://raw.githubusercontent.com/Sholahuddinoob/Bike-Sharing-Dataset/main/data/hour.csv"

day_df = pd.read_csv(day_url)
hour_df = pd.read_csv(hour_url)

# Konversi kolom tanggal
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

st.title("Bike Sharing Dashboard")
st.write("Dashboard ini menyajikan visualisasi dan analisis dari dataset Bike Sharing.")

# Fitur Interaktif: Filter berdasarkan rentang tanggal
st.sidebar.header("Filter Data")
date_range = st.sidebar.date_input("Pilih Rentang Tanggal", (day_df['dteday'].min(), day_df['dteday'].max()))

# Fitur Interaktif: Filter berdasarkan musim
season_options = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
selected_season = st.sidebar.selectbox("Pilih Musim", options=list(season_options.keys()), format_func=lambda x: season_options[x])

# Fitur Interaktif: Filter berdasarkan cuaca
weather_options = {1: "Clear", 2: "Mist", 3: "Light Rain", 4: "Heavy Rain"}
selected_weather = st.sidebar.selectbox("Pilih Cuaca", options=list(weather_options.keys()), format_func=lambda x: weather_options[x])

# Terapkan filter pada dataset
filtered_df = day_df[(day_df['dteday'] >= pd.to_datetime(date_range[0])) & 
                      (day_df['dteday'] <= pd.to_datetime(date_range[1])) & 
                      (day_df['season'] == selected_season) & 
                      (day_df['weathersit'] == selected_weather)]

# Faktor yang Mempengaruhi Peminjaman
st.header("Faktor yang Mempengaruhi Peminjaman")
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x="season", y="cnt", data=filtered_df, estimator=np.sum, palette="Blues", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_title("Total Peminjaman Sepeda Berdasarkan Musim")
ax.set_xticks(range(4))
ax.set_xticklabels(["Spring", "Summer", "Fall", "Winter"])
st.pyplot(fig)

# Scatter Plot: Hubungan Suhu dan Peminjaman
st.header("Hubungan Suhu dan Peminjaman")
fig, ax = plt.subplots(figsize=(8,5))
sns.scatterplot(x="temp", y="cnt", data=filtered_df, alpha=0.5, ax=ax)
ax.set_xlabel("Suhu")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.set_title("Hubungan Suhu dan Peminjaman Sepeda")
st.pyplot(fig)

# Boxplot: Distribusi Peminjaman Sepeda Berdasarkan Hari Kerja/Libur
st.header("Distribusi Peminjaman Berdasarkan Hari Kerja")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x="workingday", y="cnt", data=filtered_df, palette="coolwarm", ax=ax)
ax.set_xlabel("Hari Kerja (0 = Libur, 1 = Kerja)")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.set_title("Distribusi Peminjaman Sepeda Berdasarkan Hari Kerja")
st.pyplot(fig)

# Heatmap Korelasi Faktor-Faktor terhadap Peminjaman Sepeda
st.header("Korelasi Faktor-Faktor terhadap Peminjaman")
fig, ax = plt.subplots(figsize=(10,6))
corr_matrix = filtered_df[["cnt", "temp", "hum", "windspeed", "season", "weathersit", "workingday"]].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
ax.set_title("Korelasi Faktor-Faktor terhadap Peminjaman Sepeda")
st.pyplot(fig)

# Ringkasan Insight
st.header("Ringkasan Insight")
st.write("1. Musim dan kondisi cuaca memiliki pengaruh signifikan terhadap jumlah peminjaman sepeda. Musim gugur memiliki peminjaman tertinggi, sedangkan cuaca buruk menurunkan jumlah peminjaman.")
st.write("2. Suhu memiliki korelasi positif dengan peminjaman sepeda. Semakin hangat suhu, semakin tinggi jumlah peminjaman, sementara faktor seperti kelembaban dan kecepatan angin memiliki pengaruh yang lebih kecil.")
