import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Konfigurasi Dashboard ---
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# --- Load Dataset ---
@st.cache_data
def load_data():
    # Pastikan path dataset relatif
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "day.csv")
    
    df = pd.read_csv(file_path)
    df['dteday'] = pd.to_datetime(df['dteday'])  
    return df

df = load_data()

# --- Sidebar untuk Filter ---
st.sidebar.header("Filter Data")
date_range = st.sidebar.date_input("Pilih Rentang Tanggal", 
                                   [df['dteday'].min(), df['dteday'].max()])

# Validasi input tanggal
if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
elif isinstance(date_range, (list, tuple)):
    start_date = end_date = date_range[0]
else:
    st.error("Harap pilih tanggal yang valid.")
    st.stop()

# Filter berdasarkan tanggal
df_filtered = df[(df['dteday'] >= pd.to_datetime(start_date)) & 
                 (df['dteday'] <= pd.to_datetime(end_date))]

# --- Statistik Penyewaan ---
st.title("🚲 Bike Sharing Dashboard")
st.subheader("📊 Statistik Penyewaan")

col1, col2, col3 = st.columns(3)
col1.metric("Total Penyewaan", f"{df_filtered['cnt'].sum():,}")
col2.metric("Penyewaan Rata-rata", f"{df_filtered['cnt'].mean():.0f}")
col3.metric("Penyewaan Maksimum", f"{df_filtered['cnt'].max():,}")

# --- 1. Tren Penyewaan Sepeda Harian ---
st.subheader("📊 Tren Penyewaan Sepeda Harian")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df_filtered['dteday'], df_filtered['cnt'], marker='o', linestyle='-', color='b', alpha=0.7)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.set_title("Tren Penyewaan Sepeda Harian")
plt.xticks(rotation=45)
st.pyplot(fig)

# --- 2. Peminjaman Berdasarkan Musim ---
st.subheader("🌤 Peminjaman Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x='season', y='cnt', data=df_filtered, errorbar=None, palette="Blues", ax=ax)
ax.set_xticklabels(["Spring", "Summer", "Fall", "Winter"])
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_title("Jumlah Peminjaman Sepeda Berdasarkan Musim")
st.pyplot(fig)

# --- 3. Peminjaman Berdasarkan Kondisi Cuaca ---
st.subheader("🌧 Peminjaman Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x='weathersit', y='cnt', data=df_filtered, errorbar=None, palette="coolwarm", ax=ax)
ax.set_xticklabels(["Cerah", "Berawan", "Hujan Ringan", "Hujan Lebat"])
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_title("Jumlah Peminjaman Sepeda Berdasarkan Kondisi Cuaca")
st.pyplot(fig)

# --- 4. Peminjaman Berdasarkan Hari Kerja / Hari Libur ---
st.subheader("📅 Peminjaman Berdasarkan Hari Kerja / Hari Libur")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x='workingday', y='cnt', data=df_filtered, errorbar=None, palette="Set2", ax=ax)
ax.set_xticklabels(["Hari Libur", "Hari Kerja"])
ax.set_xlabel("Kategori Hari")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_title("Perbandingan Peminjaman Sepeda pada Hari Kerja & Libur")
st.pyplot(fig)

# --- 5. Korelasi Antar Variabel ---
st.subheader("📈 Korelasi Antar Variabel")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df_filtered.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)

# --- Footer ---
st.markdown("🚀 **Dashboard dibuat dengan Streamlit** | 📊 **Data: Bike Sharing Dataset**")
