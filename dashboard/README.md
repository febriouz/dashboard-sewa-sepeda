# **Dashboard Penyewaan Sepeda 🚲**

Dashboard ini adalah aplikasi interaktif berbasis **Streamlit** yang digunakan untuk menganalisis data penyewaan sepeda. Dashboard ini menampilkan berbagai visualisasi yang berguna untuk memahami tren penyewaan sepeda berdasarkan cuaca, musim, hari kerja, dan faktor lingkungan lainnya.

---

## **Fitur Utama**
- **Ringkasan Data**: Menampilkan contoh data penyewaan sepeda yang difilter.
- **Analisis Berdasarkan Cuaca**: Visualisasi jumlah penyewaan berdasarkan kondisi cuaca.
- **Analisis Hari Kerja vs Akhir Pekan**: Membandingkan rata-rata penyewaan sepeda pada hari kerja dan akhir pekan.
- **Analisis Berdasarkan Musim**: Menampilkan rata-rata penyewaan sepeda berdasarkan musim.
- **Fitur Interaktif**: Filter data berdasarkan tanggal dan musim.

---

## **Dataset yang Digunakan**
1. **`cleaned_day.csv`**: Dataset harian.
2. **`cleaned_hour.csv.gz`**: Dataset per jam yang telah dikompresi.

### **Kolom dalam Dataset**
- **dteday**: Tanggal.
- **season**: Musim (1: Musim Semi, 2: Musim Panas, 3: Musim Gugur, 4: Musim Dingin).
- **yr**: Tahun (0: 2011, 1: 2012).
- **mnth**: Bulan (1-12).
- **hr**: Jam (hanya di `cleaned_hour.csv`).
- **holiday**: Apakah hari tersebut hari libur (1: Ya, 0: Tidak).
- **weekday**: Hari dalam minggu.
- **workingday**: Apakah hari kerja (1: Ya, 0: Tidak).
- **weathersit**: Kondisi cuaca:
  - 1: Cerah
  - 2: Mendung/Hujan Ringan
  - 3: Hujan Lebat
  - 4: Ekstrem
- **temp**: Suhu normalisasi.
- **atemp**: Suhu terasa (normalisasi).
- **hum**: Kelembapan (normalisasi).
- **windspeed**: Kecepatan angin (normalisasi).
- **casual**: Jumlah pengguna kasual.
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
   **a. Menggunakan `requirements.txt`**:
   - Pastikan Python 3.8+ telah terinstal.
   - Jalankan perintah berikut untuk menginstal library yang diperlukan:
     ```bash
     pip install -r requirements.txt
     ```

   **b. Instal Dependencies Secara Manual**:
   - Jika `requirements.txt` tidak berfungsi, instal dependencies satu per satu:
     ```bash
     pip install streamlit==1.39.0
     pip install pandas==2.2.3
     pip install matplotlib==3.9.2
     pip install seaborn==0.13.2
     pip install numpy==2.1.1
     ```

3. **Jalankan Aplikasi Streamlit**:
   ```bash
   streamlit run dashboard_sewa_sepeda.py
   ```

4. **Akses Dashboard**:
   - Aplikasi akan berjalan di browser melalui URL berikut:
     ```
     Local URL: http://localhost:8501
     Network URL: http://<IP_ADDRESS>:8501
     ```

---

### **2. Akses Langsung di Streamlit Cloud**
Aplikasi ini juga tersedia secara online di **Streamlit Cloud**. Klik tautan di bawah untuk mengakses dashboard:

🔗 **[Dashboard Penyewaan Sepeda](https://dashboard-sewa-sepeda-tjteaxcctfdajat64hwhmr.streamlit.app/)**

---

## **Struktur Folder**
```
dashboard/
├── cleaned_day.csv              # Dataset harian
├── cleaned_hour.csv.gz          # Dataset per jam (dalam format gzip)
├── dashboard_sewa_sepeda.py     # File utama Streamlit
├── requirements.txt             # File dependencies
└── README.md                    # Dokumentasi proyek
```

---

## **Dependencies**
Berikut adalah library yang digunakan untuk menjalankan proyek ini:

```
streamlit==1.39.0
pandas==2.2.3
matplotlib==3.9.2
seaborn==0.13.2
numpy==2.1.1
```

Pastikan library ini terinstal sebelum menjalankan aplikasi.

---

## **Lisensi**
Proyek ini dilisensikan di bawah **MIT License**. Anda bebas menggunakannya dengan tetap mencantumkan kredit kepada pengembang asli.
