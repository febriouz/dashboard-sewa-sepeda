# Dashboard Penyewaan Sepeda 🚲

Dashboard ini adalah aplikasi interaktif berbasis **Streamlit** untuk menganalisis data penyewaan sepeda. Dashboard ini memberikan wawasan penting mengenai tren penyewaan sepeda berdasarkan cuaca, musim, suhu, kelembapan, dan waktu.

---

## **Fitur Utama**
- **Ringkasan Data**: 
  Menampilkan total penyewaan, pengguna casual, dan pengguna terdaftar.
- **Analisis Berdasarkan Cuaca**: 
  Visualisasi jumlah penyewaan berdasarkan kondisi cuaca.
- **Analisis Hari Kerja vs Akhir Pekan**: 
  Membandingkan jumlah penyewaan antara hari kerja dan akhir pekan.
- **Rata-rata Penyewaan per Jam**: 
  Tren penyewaan berdasarkan jam dalam sehari.
- **Distribusi Penyewaan Berdasarkan Suhu dan Kelembapan**: 
  Scatterplot untuk mengeksplorasi hubungan antara suhu/kelembapan dan jumlah penyewaan.

---

## **Data Set**
Dashboard ini menggunakan dua dataset yang telah dibersihkan:
1. **`cleaned_day.csv`**: Dataset harian.
2. **`cleaned_hour.csv`**: Dataset per jam.

### **Kolom dalam Dataset**
- **instant**: Indeks data.
- **dteday**: Tanggal.
- **season**: Musim (1: musim semi, 2: musim panas, 3: musim gugur, 4: musim dingin).
- **yr**: Tahun (0: 2011, 1: 2012).
- **mnth**: Bulan (1-12).
- **hr**: Jam (0-23, hanya tersedia di `cleaned_hour.csv`).
- **holiday**: Apakah hari libur (1: ya, 0: tidak).
- **weekday**: Hari dalam minggu.
- **workingday**: Apakah hari kerja (1: ya, 0: tidak).
- **weathersit**: Kondisi cuaca (1: cerah, 2: mendung, 3: hujan ringan, 4: hujan lebat).
- **temp**: Suhu normalisasi.
- **atemp**: Suhu terasa (normalisasi).
- **hum**: Kelembapan (normalisasi).
- **windspeed**: Kecepatan angin (normalisasi).
- **casual**: Jumlah pengguna casual.
- **registered**: Jumlah pengguna terdaftar.
- **cnt**: Total penyewaan sepeda (casual + registered).

---

## **Cara Menjalankan Aplikasi**
### **Secara Lokal**
1. **Clone Repository**:
   ```bash
   git clone https://github.com/username/dashboard-sewa-sepeda.git
   cd dashboard-sewa-sepeda
