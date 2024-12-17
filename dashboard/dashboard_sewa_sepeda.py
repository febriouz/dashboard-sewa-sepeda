import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    # Path file disesuaikan untuk berada di folder 'dashboard'
    hour_df = pd.read_csv('dashboard/cleaned_hour.csv')  
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    hour_df['day_type'] = hour_df['workingday'].apply(lambda x: 'Hari Kerja' if x == 1 else 'Akhir Pekan')
    
    # Menambahkan label cuaca
    weather_labels = {
        1: 'Cerah', 
        2: 'Mendung/Hujan Ringan', 
        3: 'Hujan Lebat', 
        4: 'Ekstrem'
    }
    hour_df['weathersit'] = hour_df['weathersit'].map(weather_labels)
    return hour_df

# Load data
data = load_data()

# Sidebar untuk Navigasi
st.sidebar.title("Navigasi Dashboard")
page = st.sidebar.radio("Pilih Halaman:", ["Beranda", "Analisis Cuaca", "Analisis Hari Kerja"])

# Halaman 1: Beranda
if page == "Beranda":
    st.title("Dashboard Analisis Penyewaan Sepeda 🚲")
    st.write("Dashboard ini menampilkan hasil analisis terkait faktor cuaca dan tipe hari.")
    st.subheader("Contoh Data:")
    st.dataframe(data.head(10))

# Halaman 2: Analisis Cuaca
elif page == "Analisis Cuaca":
    st.title("Pengaruh Cuaca terhadap Penyewaan Sepeda")
    avg_weather = data.groupby('weathersit')['cnt'].mean().reset_index()
    st.subheader("Rata-rata Penyewaan Berdasarkan Cuaca")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=avg_weather, x='weathersit', y='cnt', palette='Blues_d', ax=ax)
    plt.xlabel("Kondisi Cuaca")
    plt.ylabel("Rata-rata Penyewaan Sepeda")
    plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
    st.pyplot(fig)

# Halaman 3: Analisis Hari Kerja
elif page == "Analisis Hari Kerja":
    st.title("Perbandingan Penyewaan pada Hari Kerja dan Akhir Pekan")
    avg_day = data.groupby('day_type')['cnt'].mean().reset_index()
    st.subheader("Rata-rata Penyewaan Berdasarkan Tipe Hari")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=avg_day, x='day_type', y='cnt', palette='Set2', ax=ax)
    plt.xlabel("Tipe Hari")
    plt.ylabel("Rata-rata Penyewaan Sepeda")
    plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Hari Kerja dan Akhir Pekan")
    st.pyplot(fig)
