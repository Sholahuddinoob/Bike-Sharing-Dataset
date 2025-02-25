import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
day_url = "https://raw.githubusercontent.com/Sholahuddinoob/Bike-Sharing-Dataset/main/data/day.csv"
hour_url = "https://raw.githubusercontent.com/Sholahuddinoob/Bike-Sharing-Dataset/main/data/hour.csv"

st.title("Bike Sharing Dashboard")
st.write("Dashboard ini menyajikan visualisasi dan analisis dari dataset Bike Sharing.")

# Faktor yang Mempengaruhi Peminjaman
st.header("Faktor yang Mempengaruhi Peminjaman")
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x="season", y="cnt", data=day_df, estimator=sum, palette="Blues", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_title("Total Peminjaman Sepeda Berdasarkan Musim")
st.pyplot(fig)

# Waktu Terbaik untuk Promosi
st.header("Waktu Terbaik untuk Promosi")
fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(x="hr", y="cnt", data=hour_df, estimator=sum, marker="o", color="purple", ax=ax)
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Total Peminjaman Sepeda")
ax.set_title("Pola Peminjaman Sepeda Berdasarkan Jam")
st.pyplot(fig)
