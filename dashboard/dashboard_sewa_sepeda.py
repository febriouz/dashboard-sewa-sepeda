import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    # Pastikan dataset berada di folder yang sama dengan file Python ini
    hour_df = pd.read_csv('dashboard/cleaned_hour.csv')
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    hour_df['day_type'] = hour_df['workingday'].apply(lambda x: 'Hari Kerja' if x == 1 else 'Akhir Pekan')
    weather_labels = {1: 'Cerah', 2: 'Mendung/Hujan Ringan', 3: 'Hujan Lebat', 4: 'Ekstrem'}
    hour_df['weathersit'] = hour_df['weathersit'].map(weather_labels)
    season_labels = {1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'}
    hour_df['season'] = hour_df['season'].map(season_labels)
    return hour_df

# Load data
data = load_data()

# Sidebar untuk Navigasi dan Filter
st.sidebar.title("Navigasi Dashboard")

# Filter Berdasarkan Tanggal
min_date = data['dteday'].min().date()
max_date = data['dteday'].max().date()
start_date, end_date = st.sidebar.date_input(
    label="Pilih Rentang Tanggal",
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

# Filter Berdasarkan Musim
selected_season = st.sidebar.multiselect(
    "Pilih Musim",
    options=data['season'].unique(),
    default=data['season'].unique()
)

# Menerapkan Filter
filtered_data = data[
    (data['dteday'] >= pd.Timestamp(start_date)) &
    (data['dteday'] <= pd.Timestamp(end_date)) &
    (data['season'].isin(selected_season))
]

page = st.sidebar.radio("Pilih Halaman:", ["Beranda", "Analisis Cuaca", "Analisis Hari Kerja", "Analisis Musim", "Kesimpulan"])

# Halaman Beranda
if page == "Beranda":
    st.title("Dashboard Penyewaan Sepeda 🚴")
    st.write("**Dashboard ini menampilkan hasil analisis faktor cuaca, musim, dan tipe hari pada penyewaan sepeda.**")

    st.subheader("Contoh Data yang Difilter:")
    st.dataframe(filtered_data.head(10))

# Halaman Analisis Cuaca
elif page == "Analisis Cuaca":
    st.title("Pengaruh Cuaca terhadap Penyewaan Sepeda")

    # Menghitung rata-rata penyewaan berdasarkan cuaca
    avg_weather = filtered_data.groupby('weathersit')['cnt'].mean().reset_index()
    avg_weather.columns = ['Kondisi Cuaca', 'Rata-rata Penyewaan']

    st.subheader("Rata-rata Penyewaan Berdasarkan Kondisi Cuaca")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=avg_weather, x='Kondisi Cuaca', y='Rata-rata Penyewaan', palette='Blues_d', ax=ax)
    ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca")
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    st.pyplot(fig)

# Halaman Analisis Hari Kerja
elif page == "Analisis Hari Kerja":
    st.title("Perbandingan Penyewaan pada Hari Kerja dan Akhir Pekan")

    # Menghitung rata-rata penyewaan berdasarkan tipe hari
    avg_day_type = filtered_data.groupby('day_type')['cnt'].mean().reset_index()
    avg_day_type.columns = ['Tipe Hari', 'Rata-rata Penyewaan']

    st.subheader("Rata-rata Penyewaan Berdasarkan Tipe Hari")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=avg_day_type, x='Tipe Hari', y='Rata-rata Penyewaan', palette='muted', ax=ax)
    ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Hari Kerja dan Akhir Pekan")
    ax.set_xlabel("Tipe Hari")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    st.pyplot(fig)

# Halaman Analisis Musim
elif page == "Analisis Musim":
    st.title("Pengaruh Musim terhadap Penyewaan Sepeda")

    # Menghitung rata-rata penyewaan berdasarkan musim
    avg_season = filtered_data.groupby('season')['cnt'].mean().reset_index()
    avg_season.columns = ['Musim', 'Rata-rata Penyewaan']

    st.subheader("Rata-rata Penyewaan Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=avg_season, x='Musim', y='Rata-rata Penyewaan', palette='coolwarm', ax=ax)
    ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    st.pyplot(fig)

# Halaman Kesimpulan
elif page == "Kesimpulan":
    st.title("Kesimpulan Analisis Penyewaan Sepeda")

    st.subheader("Kesimpulan Analisis Cuaca:")
    st.write("- Penyewaan sepeda tertinggi terjadi pada **cuaca cerah** dengan rata-rata **204 penyewaan**.")
    st.write("- Penyewaan sepeda menurun drastis pada **cuaca ekstrem**, hanya **74 penyewaan rata-rata**.")

    st.subheader("Kesimpulan Analisis Hari Kerja:")
    st.write("- Penyewaan pada **hari kerja** lebih tinggi dibandingkan akhir pekan, yaitu rata-rata **193 penyewaan**.")
    st.write("- Akhir pekan tetap memiliki permintaan tinggi dengan rata-rata **181 penyewaan**.")

    st.subheader("Kesimpulan Analisis Musim:")
    st.write("- Penyewaan tertinggi terjadi pada **Musim Panas**, dengan rata-rata **5644 penyewaan**.")
    st.write("- Penyewaan terendah tercatat pada **Musim Dingin**, yaitu rata-rata **2604 penyewaan**.")
