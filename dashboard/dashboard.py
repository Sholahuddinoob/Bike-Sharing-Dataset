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

st.title("Bike Sharing Dashboard")
st.write("Dashboard ini menyajikan visualisasi dan analisis dari dataset Bike Sharing.")

# Faktor yang Mempengaruhi Peminjaman
st.header("Faktor yang Mempengaruhi Peminjaman")
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x="season", y="cnt", data=day_df, estimator=np.sum, palette="Blues", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_title("Total Peminjaman Sepeda Berdasarkan Musim")
ax.set_xticks([0, 1, 2, 3])  
ax.set_xticklabels(["Spring", "Summer", "Fall", "Winter"])  # Ubah angka menjadi label musim
st.pyplot(fig)

# Waktu Terbaik untuk Promosi
st.header("Waktu Terbaik untuk Promosi")
fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(x="hr", y="cnt", data=hour_df, estimator=np.sum, marker="o", color="purple", ax=ax)
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_title("Pola Peminjaman Sepeda Berdasarkan Jam")
ax.set_xticks(range(0, 24, 3))  # Tampilkan label jam dengan interval 3
ax.grid(True, linestyle="--", alpha=0.6)  # Tambahkan grid agar lebih mudah dibaca

# Format angka di sumbu Y agar lebih jelas
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"{int(x/1000)}K"))

# Agregasi data untuk tren peminjaman berdasarkan jam
hourly_rentals = hour_df.groupby("hr")["cnt"].sum().reset_index()

fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(x="hr", y="cnt", data=hourly_rentals, marker="o", color="purple", ax=ax)
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_title("Pola Peminjaman Sepeda Berdasarkan Jam")
st.pyplot(fig)
