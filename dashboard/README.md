# **Dashboard Penyewaan Sepeda 🚲**

Dashboard ini adalah aplikasi interaktif berbasis **Streamlit** yang menganalisis data penyewaan sepeda. Aplikasi ini memberikan wawasan mengenai tren penyewaan sepeda berdasarkan cuaca, hari kerja/akhir pekan, musim, dan faktor lingkungan lainnya.

---

## **Fitur Utama**
- **Ringkasan Data**:  
  Menampilkan contoh data penyewaan sepeda yang telah difilter.
- **Analisis Berdasarkan Cuaca**:  
  Visualisasi penyewaan berdasarkan kondisi cuaca.
- **Analisis Hari Kerja vs Akhir Pekan**:  
  Membandingkan penyewaan sepeda antara hari kerja dan akhir pekan.
- **Analisis Berdasarkan Musim**:  
  Menampilkan rata-rata penyewaan berdasarkan musim.
- **Fitur Interaktif**:  
  Filter berdasarkan tanggal dan musim untuk analisis data yang lebih spesifik.

---

## **Dataset**
Dashboard ini menggunakan dua dataset yang telah dibersihkan:
1. **`cleaned_day.csv`**: Dataset harian.
2. **`cleaned_hour.csv`**: Dataset per jam.

### **Kolom dalam Dataset**
- **dteday**: Tanggal.
- **season**: Musim (1: Musim Semi, 2: Musim Panas, 3: Musim Gugur, 4: Musim Dingin).
- **yr**: Tahun (0: 2011, 1: 2012).
- **mnth**: Bulan (1-12).
- **hr**: Jam (0-23, hanya di `cleaned_hour.csv`).
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

## **Cara Mengakses Dashboard**
Dashboard ini telah dideploy secara online melalui **Streamlit Cloud**. Klik link berikut untuk langsung mengakses aplikasi:

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

---

## **Lisensi**
Proyek ini dilisensikan di bawah **MIT License**. Anda bebas menggunakannya, namun tetap mencantumkan kredit kepada pengembang asli.
