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
date_range = st.sidebar.date_input("Pilih Rentang Tanggal", 
                                   [day_df['dteday'].min(), day_df['dteday'].max()])
if isinstance(date_range, tuple):
    start_date, end_date = date_range
else:
    start_date, end_date = date_range, date_range  # Jika hanya satu tanggal, gunakan nilai yang sama

# Fitur Interaktif: Filter berdasarkan musim
season_options = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
selected_season = st.sidebar.selectbox("Pilih Musim", options=list(season_options.keys()), format_func=lambda x: season_options[x])

# Fitur Interaktif: Filter berdasarkan cuaca
weather_options = {1: "Clear", 2: "Mist", 3: "Light Rain", 4: "Heavy Rain"}
selected_weather = st.sidebar.selectbox("Pilih Cuaca", options=list(weather_options.keys()), format_func=lambda x: weather_options[x])

# Terapkan filter pada dataset
filtered_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & 
                      (day_df['dteday'] <= pd.to_datetime(end_date)) & 
                      (day_df['season'] == selected_season) & 
                      (day_df['weathersit'] == selected_weather)]

# Faktor yang Mempengaruhi Peminjaman
st.header("Faktor yang Mempengaruhi Peminjaman")
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x="season", y="cnt", data=filtered_df, estimator=np.sum, palette="Blues", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_title("Total Peminjaman Sepeda Berdasarkan Musim")
ax.set_xticks([0, 1, 2, 3])  
ax.set_xticklabels(["Spring", "Summer", "Fall", "Winter"])
st.pyplot(fig)

# Waktu Terbaik untuk Promosi
st.header("Waktu Terbaik untuk Promosi")
# Agregasi data jumlah peminjaman berdasarkan jam
hourly_rentals = hour_df.groupby("hr")["cnt"].sum().reset_index()

fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(x="hr", y="cnt", data=hourly_rentals, marker="o", color="purple", ax=ax)
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_title("Pola Peminjaman Sepeda Berdasarkan Jam")
ax.set_xticks(range(0, 24, 3))
ax.grid(True, linestyle="--", alpha=0.6)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"{int(x/1000)}K"))
st.pyplot(fig)

# Pola Peminjaman Berdasarkan Hari dalam Seminggu
st.header("Pola Peminjaman Berdasarkan Hari")
# Agregasi data jumlah peminjaman berdasarkan hari dalam seminggu
daily_rentals = filtered_df.groupby("weekday")["cnt"].sum().reset_index()

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x="weekday", y="cnt", data=daily_rentals, hue="weekday", palette="Oranges", legend=False, ax=ax)
ax.set_xlabel("Hari dalam Seminggu")
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_title("Pola Peminjaman Sepeda Berdasarkan Hari dalam Seminggu")
ax.set_xticks(range(0,7))
ax.set_xticklabels(["Ahad", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"])
st.pyplot(fig)
