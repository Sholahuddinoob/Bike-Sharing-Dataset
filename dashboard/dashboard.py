import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Judul
st.title("🚲 Bike Sharing Dashboard")

# Load Dataset dari GitHub
@st.cache_data
def load_data():
    day_url = "https://raw.githubusercontent.com/Sholahuddinoob/Bike-Sharing-Dataset/refs/heads/main/data/day.csv"
    hour_url = "https://raw.githubusercontent.com/Sholahuddinoob/Bike-Sharing-Dataset/refs/heads/main/data/hour.csv"
    
    try:
        day_df = pd.read_csv(day_url)
        hour_df = pd.read_csv(hour_url)
        return day_df, hour_df
    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
        return None, None

day_df, hour_df = load_data()

# Pastikan dataset berhasil dimuat
if day_df is None or hour_df is None:
    st.stop()

# Sidebar untuk filter data
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim:", ["Semua", "Spring", "Summer", "Fall", "Winter"])
season_dict = {"Spring": 1, "Summer": 2, "Fall": 3, "Winter": 4}

# Filter berdasarkan musim
if selected_season != "Semua":
    day_df = day_df[day_df["season"] == season_dict[selected_season]]

# Menampilkan dataframe
st.subheader("📌 Preview Dataset")
st.write(day_df.head())

# **1. Visualisasi Tren Peminjaman Sepeda**
st.subheader("📊 Tren Peminjaman Sepeda Harian")
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(x=day_df.index, y=day_df["cnt"], marker="o", linestyle="-", color="b", ax=ax)
ax.set_title("Tren Peminjaman Sepeda Harian")
ax.set_xlabel("Hari ke-")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# **2. Faktor yang Mempengaruhi Peminjaman**
st.subheader("📊 Faktor yang Mempengaruhi Peminjaman Sepeda")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**🔸 Berdasarkan Hari Kerja**")
    fig, ax = plt.subplots()
    sns.boxplot(x="workingday", y="cnt", data=day_df, palette="coolwarm", ax=ax)
    ax.set_xticklabels(["Akhir Pekan", "Hari Kerja"])
    ax.set_xlabel("Hari")
    ax.set_ylabel("Jumlah Peminjaman")
    st.pyplot(fig)

with col2:
    st.markdown("**🔸 Berdasarkan Cuaca**")
    fig, ax = plt.subplots()
    sns.boxplot(x="weathersit", y="cnt", data=day_df, palette="coolwarm", ax=ax)
    ax.set_xticklabels(["Cerah", "Berawan", "Hujan"])
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Peminjaman")
    st.pyplot(fig)

# **3. Kapan Waktu Terbaik untuk Promosi?**
st.subheader("📊 Pola Peminjaman Sepeda per Jam")
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(x="hr", y="cnt", data=hour_df, marker="o", linestyle="-", color="r", ax=ax)
ax.set_title("Pola Peminjaman Sepeda per Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

st.markdown("""
**📌 Kesimpulan:**  
1. Cuaca dan hari kerja sangat memengaruhi jumlah peminjaman sepeda.  
2. Waktu terbaik untuk meningkatkan layanan atau promosi adalah saat jam sibuk (07:00 - 09:00 & 17:00 - 19:00).
""")
