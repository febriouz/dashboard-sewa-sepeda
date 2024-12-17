

# **Dashboard Penyewaan Sepeda 🚲**

Dashboard ini adalah aplikasi interaktif berbasis **Streamlit** yang menganalisis data penyewaan sepeda. Aplikasi ini memberikan wawasan mengenai tren penyewaan sepeda berdasarkan cuaca, hari kerja/akhir pekan, suhu, dan kelembapan.

---

## **Fitur Utama**
- **Ringkasan Data**:  
  Menampilkan contoh data penyewaan sepeda.
- **Analisis Berdasarkan Cuaca**:  
  Visualisasi rata-rata penyewaan berdasarkan kondisi cuaca.
- **Analisis Hari Kerja vs Akhir Pekan**:  
  Membandingkan rata-rata penyewaan sepeda antara hari kerja dan akhir pekan.

---

## **Dataset**
Dashboard ini menggunakan dua dataset yang telah dibersihkan:
1. **`cleaned_day.csv`**: Dataset harian.
2. **`cleaned_hour.csv`**: Dataset per jam.

### **Kolom dalam Dataset**
- **instant**: Indeks data.
- **dteday**: Tanggal.
- **season**: Musim (1: musim semi, 2: musim panas, 3: musim gugur, 4: musim dingin).
- **yr**: Tahun (0: 2011, 1: 2012).
- **mnth**: Bulan (1-12).
- **hr**: Jam (hanya tersedia di `cleaned_hour.csv`).
- **holiday**: Hari libur (1: ya, 0: tidak).
- **weekday**: Hari dalam minggu.
- **workingday**: Hari kerja (1: ya, 0: tidak).
- **weathersit**: Kondisi cuaca:  
   - 1: Cerah,  
   - 2: Mendung/Hujan Ringan,  
   - 3: Hujan Lebat,  
   - 4: Ekstrem.  
- **temp**: Suhu normalisasi.
- **atemp**: Suhu terasa (normalisasi).
- **hum**: Kelembapan (normalisasi).
- **windspeed**: Kecepatan angin (normalisasi).
- **casual**: Jumlah pengguna casual.
- **registered**: Jumlah pengguna terdaftar.
- **cnt**: Total penyewaan sepeda (casual + registered).

---

## **Cara Menjalankan Aplikasi**
### **1. Menjalankan Secara Lokal**
1. **Clone Repository**:
   ```bash
   git clone https://github.com/febriouz/dashboard-sewa-sepeda.git
   cd dashboard-sewa-sepeda/dashboard
   ```

2. **Install Dependencies**:  
   - Pastikan Python 3.8+ sudah terinstal.
   - Install library yang dibutuhkan menggunakan file `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

3. **Jalankan Aplikasi Streamlit**:
   ```bash
   streamlit run dashboard_sewa_sepeda.py
   ```

4. **Akses Dashboard**:
   - Aplikasi akan berjalan di browser melalui URL:  
     ```
     http://localhost:8501
     ```

---

### **2. Akses Langsung di Streamlit Cloud**
Aplikasi ini tersedia secara online di **Streamlit Cloud**. Anda bisa langsung mengakses dashboard melalui link berikut:

🔗 **[Dashboard Penyewaan Sepeda](https://dashboard-sewa-sepeda-tjteaxcctfdajat64hwhmr.streamlit.app/)**

---

## **Struktur Folder**
```
dashboard/
├── cleaned_day.csv              # Dataset harian
├── cleaned_hour.csv             # Dataset per jam
├── dashboard_sewa_sepeda.py     # File utama Streamlit
├── requirements.txt             # File dependencies
└── README.md                    # Dokumentasi proyek
```

---

## **Dependencies**
Aplikasi ini menggunakan library berikut:
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Seaborn**

Pastikan library ini diinstal melalui file `requirements.txt`.

---

## **Lisensi**
Proyek ini berlisensi **MIT**. Anda bebas menggunakannya, namun tetap mencantumkan kredit kepada penulis.


