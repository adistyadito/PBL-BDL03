import streamlit as st
import altair as alt
import pandas as pd
from PIL import Image
import warnings
import requests 
from io import BytesIO

warnings.filterwarnings('ignore')

# Konfigurasi halaman
st.set_page_config(layout="wide", page_title="Dashboard", initial_sidebar_state="auto")


def load_data():
    return pd.read_csv(
        "https://raw.githubusercontent.com/adistyadito/PBL-BDL03/refs/heads/main/StudentPredDataa.csv",
        sep=",",
        on_bad_lines='skip'
    )

def display_logo():
    # URL gambar online
    url = 'https://raw.githubusercontent.com/adistyadito/PBL-BDL03/refs/heads/main/streamlit/University_of_Malaya-Logo.wine.png'
    
    # Mengambil gambar dari URL
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    
    # Membuat kolom untuk menampilkan gambar dan judul
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
        st.image(image, width=500)
    with col2:
        st.title("Dashboard Performa Mahasiswa")

def preview_data(df):
    with st.expander("Data Preview"):
        col1, col2, col3 = st.columns(3)

        # Tambahkan filter berdasarkan Gender dan Semester
        with col1:
            gender_filter = st.multiselect("Filter Gender:", options=df['Gender'].unique(), default=[], key='gender_filter1')

        with col2:
            semester_filter = st.multiselect("Filter Semester:", options=df['Semester'].unique(), default=[], key='semester_filter1')

        with col3:
            department_filter = st.multiselect("Filter Department:", options=df['Department'].unique(), default=[], key='department_filter1')
        
        # Filter data
        if gender_filter and semester_filter and department_filter:  # Jika ada filter yang dipilih
            filtered_df = df[(df['Gender'].isin(gender_filter)) & (df['Semester'].isin(semester_filter)) & (df['Department'].isin(department_filter))]
        elif gender_filter:  # Jika hanya gender yang dipilih
            filtered_df = df[df['Gender'].isin(gender_filter)]
        elif semester_filter:  # Jika hanya semester yang dipilih
            filtered_df = df[df['Semester'].isin(semester_filter)]
        elif department_filter:  # Jika hanya department yang dipilih
            filtered_df = df[df['Department'].isin(department_filter)]
        else:  # Jika tidak ada filter yang dipilih, tampilkan semua data
            filtered_df = df

        st.dataframe(filtered_df)

def plot_distribution(df):
   with st.expander("Plot Frekuensi", expanded=True):
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Last:Q", bin=True, title="GPA"),
        y=alt.Y('count()', title='Jumlah Mahasiswa'),
        color=alt.value('steelblue')
    ).properties(
        width=800,
        height=400,
        title="Frekuensi GPA"
    )
    st.altair_chart(chart, use_container_width=True)

    freq_gender_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Gender:N', title="Gender"),
        y=alt.Y('count()', title='Jumlah Mahasiswa'),
        color=alt.value('steelblue')
    ).properties(
        width=800,
        height=400,
        title="Frekuensi Gender"
    )
    st.altair_chart(freq_gender_chart, use_container_width=True)
    
    freq_dept_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Department:N', title="Jurusan"),
        y=alt.Y('count()', title='Jumlah Mahasiswa'),
        color=alt.value('steelblue')
    ).properties(
        width=800,
        height=400,
        title="Frekuensi Jurusan"
    )
    st.altair_chart(freq_dept_chart, use_container_width=True)

    freq_hometown_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Hometown:N', title="Tempat Asal"),
        y=alt.Y('count()', title='Jumlah Mahasiswa'),
        color=alt.value('steelblue')
    ).properties(
        width=800,
        height=400,
        title="Frekuensi Tempat Asal"
    ) 
    st.altair_chart(freq_hometown_chart, use_container_width=True)

    freq_income_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Income:N', title="Pendapatan"),
        y=alt.Y('count()', title='Jumlah Mahasiswa'),
        color=alt.value('steelblue')
    ).properties(
        width=800,
        height=400,
        title="Frekuensi Pendapatan"
    )
    st.altair_chart(freq_income_chart, use_container_width=True)

    freq_preparation_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Preparation:N', title="Persiapan"),
        y=alt.Y('count()', title='Jumlah Mahasiswa'),
        color=alt.value('steelblue')
    ).properties(
        width=800,
        height=400,
        title="Frekuensi Persiapan"
    )
    st.altair_chart(freq_preparation_chart, use_container_width=True)

    freq_gaming_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Gaming:N', title="Gaming"),
        y=alt.Y('count()', title='Jumlah Mahasiswa'),
        color=alt.value('steelblue')
    ).properties(
        width=800,
        height=400,
        title="Frekuensi Gaming"
    )
    st.altair_chart(freq_gaming_chart, use_container_width=True)

    freq_attendance_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Attendance:N', title="Kehadiran"),
        y=alt.Y('count()', title='Jumlah Mahasiswa'),
        color=alt.value('steelblue')
    ).properties(
        width=800,
        height=400,
        title="Frekuensi Kehadiran"
    )
    st.altair_chart(freq_attendance_chart, use_container_width=True)

    freq_job_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Job:N', title="Pekerjaan"),
        y=alt.Y('count()', title='Jumlah Mahasiswa'),
        color=alt.value('steelblue')
    ).properties(
        width=800,
        height=400,
        title="Frekuensi Pekerjaan"
    )
    st.altair_chart(freq_job_chart, use_container_width=True)

    freq_extra_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Extra:N', title="Ekstrakulikuler"),
        y=alt.Y('count()', title='Jumlah Mahasiswa'),
        color=alt.value('steelblue')
    ).properties(
        width=800,
        height=400,
        title="Frekuensi Ekstrakulikuler"
    )
    st.altair_chart(freq_extra_chart, use_container_width=True)


def plot_distributinby(df):
    with st.expander("Distribution Plot", expanded=True):
        gender_dist_dept = alt.Chart(df).mark_bar().encode(
            x='Department:N',
            y='count():Q',
            color=alt.Color('Gender:N', legend=None)
        ).interactive().properties(
            width=800,
            height=400,
            title="Distribusi Gender berdasarkan Jurusan"
        )
        st.altair_chart(gender_dist_dept, use_container_width=True)

        attendance_dist_prep = alt.Chart(df).mark_bar().encode(
            x='Preparation:N',
            y='count():Q',
            color=alt.Color('Attendance:N', legend=None)
        ).interactive().properties(
            width=800,
            height=400,
            title="Distribusi Persiapan berdasarkan Kehadiran"
        )
        st.altair_chart(attendance_dist_prep, use_container_width=True)

        # Pie Chart
        preparation_counts = df["Preparation"].value_counts().reset_index()
        preparation_counts.columns = ['Preparation', 'Count']
        preparation_counts['percentage'] = preparation_counts['Count'] / preparation_counts['Count'].sum() * 100

        dist_prep_time = alt.Chart(preparation_counts).mark_arc().encode(
            theta=alt.Theta(field="Count", type="quantitative", stack="normalize"),  # Normalisasi untuk pie chart
            color=alt.Color("Preparation:N", legend=None),  # Warna berdasarkan kategori Preparation
            tooltip=["Preparation:N", "Count:Q", "percentage:Q"],  # Menampilkan tooltip saat hover
            text=alt.Text("percentage:Q", format=".1f")  # Menambahkan label persentase pada setiap segmen
        ).properties(
            width=800,
            height=400,
            title="Distribusi Persiapan"
        )
        st.altair_chart(dist_prep_time, use_container_width=True)

        job_dist_prep = alt.Chart(df).mark_bar().encode(
            x='Preparation:N',
            y='count():Q',
            color=alt.Color('Job:N', legend=None)
        ).interactive().properties(
            width=800,
            height=400,
            title="Distribusi Persiapan berdasarkan Pekerjaan"
        )
        st.altair_chart(job_dist_prep, use_container_width=True)

        job_dist_attendance = alt.Chart(df).mark_bar().encode(
            x='Attendance:N',
            y='count():Q',
            color=alt.Color('Job:N', legend=None)
        ).interactive().properties(
            width=800,
            height=400,
            title="Distribusi Kehadiran berdasarkan Pekerjaan"
        )
        st.altair_chart(job_dist_attendance, use_container_width=True)

        gaming_dist_prep = alt.Chart(df).mark_bar().encode(
            x='Preparation:N',
            y='count():Q',
            color=alt.Color('Gaming:N', legend=None)
        ).interactive().properties(
            width=800,
            height=400,
            title="Distribusi Persiapan berdasarkan Gaming"
        )
        st.altair_chart(gaming_dist_prep, use_container_width=True)

        extra_dist_attendance = alt.Chart(df).mark_bar().encode(
            x='Attendance:N',
            y='count():Q',
            color=alt.Color('Extra:N', legend=None)
        ).interactive().properties(
            width=800,
            height=400,
            title="Distribusi Kehadiran berdasarkan Ekstrakulikuler"
        )
        st.altair_chart(extra_dist_attendance, use_container_width=True)

        extra_dist_prep = alt.Chart(df).mark_bar().encode(
            x='Preparation:N',
            y='count():Q',
            color=alt.Color('Extra:N', legend=None)
        ).interactive().properties(
            width=800,
            height=400,
            title="Distribusi Persiapan berdasarkan Ekstrakulikuler"
        )
        st.altair_chart(extra_dist_prep, use_container_width=True)

        

def run_dashboard():
    # Judul halaman
    #st.title("Overview")

    # Load Data
    df = load_data()

    # Tambahkan gaya
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

    # Display logo
    display_logo()

    # Preview Data
    preview_data(df)

    # Visualisasi Data
    plot_distribution(df)
    plot_distributinby(df)

# Jalankan dashboard
run_dashboard()
