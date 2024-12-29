import streamlit as st
import altair as alt
import pandas as pd
from PIL import Image
import warnings

warnings.filterwarnings('ignore')

# Konfigurasi halaman (WAJIB di awal)
st.set_page_config(layout="wide")

def run_dashboard():
    # Judul halaman
    st.title("Overview")

    # Baca dataset
    df = pd.read_csv(
        "C:/Users/USER/Downloads/PBL PROJECT 888 GACOR/StudentPredDataa.csv",
        sep=",",
        on_bad_lines='skip'
    )    

    # Tambahkan gaya
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

    # Memuat logo
    image = Image.open('C:/Users/USER/Downloads/PBL PROJECT 888 GACOR/PBL PROJECT 888 GACOR/University_of_Malaya-Logo.wine.png')  # Sesuaikan path gambar

    # Header dengan logo
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
        st.image(image, width=100)
    with col2:
        st.title("Dashboard Performa Mahasiswa")

    # Visualisasi Data dengan Altair
    st.subheader("Distribusi Nilai Overall")
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Overall:Q", bin=True, title="Overall Score"),
        y=alt.Y('count()', title='Jumlah Mahasiswa'),
        color=alt.value('steelblue')
    ).properties(
        width=800,
        height=400,
        title="Distribusi Nilai Overall"
    )
    st.altair_chart(chart, use_container_width=True)

    # Grafik kedua: Attendance vs GPA
    st.subheader("Preparation")
    scatter_chart = alt.Chart(df).mark_bar(size=60).encode(
        x='Preparation:N',
        y='count():Q',
        color=alt.Color('Preparation:N', legend=None)
    ).interactive().properties(
        width=800,
        height=400,
        title="Preparation Count"
    )
    st.altair_chart(scatter_chart, use_container_width=True)

    # Grafik ketiga: Distribusi Gender
    st.subheader("Distribusi Gender")
    gender_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Gender:N', title="Gender"),
        y=alt.Y('count()', title='Jumlah Mahasiswa'),
        color=alt.Color('Gender:N', legend=None)
    ).properties(
        width=800,
        height=400,
        title="Distribusi Gender"
    )
    st.altair_chart(gender_chart, use_container_width=True)


    # Box Plot untuk distribusi GPA berdasarkan Semester
    box_plot = alt.Chart(df).mark_boxplot().encode(
        x='Semester:O',  # Semester di sumbu X
        y='Last:Q',  # GPA di sumbu Y
        tooltip=['Semester', 'Last']  # Tooltip untuk melihat nilai Semester dan GPA
    ).properties(
        title='Distribusi GPA Berdasarkan Semester'
    )

    # Menampilkan plot di Streamlit
    st.altair_chart(box_plot, use_container_width=True)

    st.write(df)