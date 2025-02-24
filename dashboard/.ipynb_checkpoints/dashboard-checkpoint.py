import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Konfigurasi Dashboard ---
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# --- Load Dataset ---
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\Sholahuddin\Documents\Submission1-Sholahuddin\data\day.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])  
    return df

df = load_data()

# --- Sidebar untuk Filter ---
st.sidebar.header("Filter Data")
date_range = st.sidebar.date_input("Pilih Rentang Tanggal", 
                                   [df['dteday'].min(), df['dteday'].max()])

# --- Perbaikan untuk Mencegah IndexError ---
if isinstance(date_range, tuple) or isinstance(date_range, list):  
    if len(date_range) == 2:  # Jika pengguna memilih rentang tanggal
        start_date, end_date = date_range
    else:  # Jika hanya satu tanggal dipilih
        start_date = end_date = date_range[0]
else:  # Jika Streamlit hanya mengembalikan satu tanggal (bukan tuple/list)
    start_date = end_date = date_range

# Konversi ke format datetime dan lakukan filter
df_filtered = df[(df['dteday'] >= pd.to_datetime(start_date)) & 
                 (df['dteday'] <= pd.to_datetime(end_date))]

# --- Judul Dashboard ---
st.title("🚲 Bike Sharing Dashboard")

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

# --- 4. Korelasi Antar Variabel ---
st.subheader("📈 Korelasi Antar Variabel")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df_filtered.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)

# ✅ **Fitur Tambahan: Statistik Ringkasan**
st.sidebar.subheader("📊 Statistik Data")
st.sidebar.write(f"**Total Data**: {len(df_filtered)}")
st.sidebar.write(f"**Rata-rata Peminjaman Sepeda**: {df_filtered['cnt'].mean():,.2f}")
st.sidebar.write(f"**Peminjaman Maksimum**: {df_filtered['cnt'].max():,}")
st.sidebar.write(f"**Peminjaman Minimum**: {df_filtered['cnt'].min():,}")

# ✅ **Fitur Tambahan: Perbandingan Hari Kerja & Akhir Pekan**
st.subheader("📅 Perbandingan Peminjaman: Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots(figsize=(6, 4))
sns.barplot(x="workingday", y="cnt", data=df_filtered, errorbar=None, palette="Set2", ax=ax)
ax.set_xticklabels(["Akhir Pekan", "Hari Kerja"])
ax.set_xlabel("Tipe Hari")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_title("Peminjaman Sepeda: Hari Kerja vs Akhir Pekan")
st.pyplot(fig)

# ✅ **Fitur Tambahan: Pilihan Tampilan Data (Tabel)**
st.subheader("📋 Data Tabel")
show_table = st.checkbox("Tampilkan Data Tabel")
if show_table:
    st.dataframe(df_filtered)

# --- Footer ---
st.markdown("🚀 **Dashboard dibuat dengan Streamlit** | 📊 **Data: Bike Sharing Dataset**")
