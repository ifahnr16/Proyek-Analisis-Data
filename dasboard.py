import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
day_data = pd.read_csv('day.csv')  # Pastikan file day.csv berada di direktori yang sama
hour_data = pd.read_csv('hour.csv')  # Pastikan file hour.csv berada di direktori yang sama

# Dashboard Title
st.title("Dashboard Analisis Data Penyewaan Sepeda")

# Sidebar Navigation
st.sidebar.title("Navigasi")
options = st.sidebar.radio("Pilih Halaman:", ["Overview Dataset", "Analisis Musiman", "Analisis Hari Kerja vs Libur", "Korelasi Antar Variabel"])

# 1. Overview Dataset
if options == "Overview Dataset":
    st.header("Overview Dataset")
    st.subheader("Preview Data Harian")
    st.dataframe(day_data.head())

    st.subheader("Informasi Dataset")
    st.text(f"Jumlah Baris: {day_data.shape[0]}")
    st.text(f"Jumlah Kolom: {day_data.shape[1]}")
    
    st.subheader("Statistik Deskriptif")
    st.dataframe(day_data.describe())

# 2. Analisis Musiman
elif options == "Analisis Musiman":
    st.header("Analisis Musiman")
    avg_rentals_by_season = day_data.groupby('season')['cnt'].mean().reset_index()
    
    fig, ax = plt.subplots()
    sns.barplot(x='season', y='cnt', data=avg_rentals_by_season, ax=ax)
    ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Musim')
    ax.set_xlabel('Musim (1: Semi, 2: Panas, 3: Gugur, 4: Dingin)')
    ax.set_ylabel('Rata-rata Penyewaan')
    st.pyplot(fig)

# 3. Analisis Hari Kerja vs Libur
elif options == "Analisis Hari Kerja vs Libur":
    st.header("Analisis Hari Kerja vs Hari Libur")
    avg_rentals_by_workingday = day_data.groupby('workingday')['cnt'].mean().reset_index()
    
    fig, ax = plt.subplots()
    sns.barplot(x='workingday', y='cnt', data=avg_rentals_by_workingday, ax=ax)
    ax.set_title('Rata-rata Penyewaan Sepeda: Hari Kerja vs Hari Libur')
    ax.set_xlabel('Hari Kerja (1) vs Hari Libur (0)')
    ax.set_ylabel('Rata-rata Penyewaan')
    st.pyplot(fig)

# 4. Korelasi Antar Variabel
elif options == "Korelasi Antar Variabel":
    st.header("Korelasi Antar Variabel")
    numeric_data = day_data.select_dtypes(include=['number'])
    
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title('Korelasi Antar Variabel')
    st.pyplot(fig)
