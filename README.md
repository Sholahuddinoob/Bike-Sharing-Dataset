# 🚲 Bike Sharing Dashboard  

Dashboard interaktif ini dibuat menggunakan **Streamlit** untuk menganalisis **Bike Sharing Dataset**. Dashboard ini membantu dalam memahami pola peminjaman sepeda berdasarkan berbagai faktor seperti cuaca, hari kerja, dan waktu.  

## 📂 Struktur Direktori  

Submission_Bike_Sharing/
│── dashboard/
│ ├── dashboard.py # File utama untuk Streamlit Dashboard
│── data/
│ ├── day.csv # Dataset utama yang digunakan
│── notebook.ipynb # Jupyter Notebook untuk EDA & analisis
│── README.md # Panduan cara menjalankan dashboard
│── requirements.txt # Library yang digunakan
│── url.txt # URL Streamlit Cloud (jika dideploy)

## 🚀 Cara Menjalankan Dashboard  

### 1️⃣ **Persiapan Awal**  
Pastikan **Python** dan **pip** sudah terinstall di sistem Anda.  
Jika belum, silakan install Python dari [python.org](https://www.python.org/downloads/).  

### 2️⃣ **Clone Repository & Install Dependencies**  
Jalankan perintah berikut di terminal atau command prompt:  

```sh
git clone https://github.com/Sholahuddinoob/Bike-Sharing-Dataset.git
cd Bike-Sharing-Dataset
pip install -r requirements.txt
```

3️⃣ Menjalankan Streamlit
Untuk menjalankan dashboard, gunakan perintah berikut:

sh
Salin
Edit
streamlit run dashboard/dashboard.py
Setelah dijalankan, buka browser dan akses:
🔗 http://localhost:8501
