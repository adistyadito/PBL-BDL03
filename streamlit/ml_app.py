import streamlit as st
import joblib
import os
import requests

# Fungsi untuk mendownload model dari GitHub
def download_model(url, model_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Untuk memeriksa status kode 200
        with open(model_path, 'wb') as file:
            file.write(response.content)
        st.success("Model berhasil didownload.")
    except requests.exceptions.RequestException as e:
        st.error(f"Terjadi kesalahan saat mendownload model: {e}")

# Fungsi Prediksi dengan Model ML
def predict_status(last_gpa, preparation_0_1_hour, preparation_2_3_hours, preparation_more_than_3_hours, 
                   attendance_80_100, attendance_60_79, attendance_40_59, attendance_below_40, semester):
    model_path = 'student_mod.pkl'

    # Mengecek apakah model sudah ada, jika tidak download
    if not os.path.exists(model_path):
        model_url = "https://github.com/adistyadito/PBL-BDL03/raw/refs/heads/main/streamlit/student_mod.pkl"
        download_model(model_url, model_path)
    
    if os.path.exists(model_path):
        model = joblib.load(model_path)
    else:
        st.error("Model tidak ditemukan! Harap tambahkan model yang valid.")
        return "Error"

    # Format input untuk model
    input_data = [[last_gpa, preparation_0_1_hour, preparation_2_3_hours, preparation_more_than_3_hours, 
                   attendance_80_100, attendance_60_79, attendance_40_59, attendance_below_40, semester]]
    prediction = model.predict(input_data)

    return prediction[0]


# Fungsi Utama Streamlit
def run_ml_app():
    st.title('Analisis Performa Mahasiswa')

    # Input Data berdasarkan Feature Importance
    st.subheader("Masukkan Data Anda")

    last_gpa = st.number_input('Last GPA (0.0 - 4.0)', min_value=0.0, max_value=4.0, value=2.5, step=0.1)

    preparation = st.selectbox('Preparation Time', ['0-1 Hour', '2-3 Hours', 'More than 3 Hours'])
    preparation_0_1_hour = 1 if preparation == '0-1 Hour' else 0
    preparation_2_3_hours = 1 if preparation == '2-3 Hours' else 0
    preparation_more_than_3_hours = 1 if preparation == 'More than 3 Hours' else 0

    attendance = st.selectbox('Attendance', ['80%-100%', '60%-79%', '40%-59%', 'Below 40%'])
    attendance_80_100 = 1 if attendance == '80%-100%' else 0
    attendance_60_79 = 1 if attendance == '60%-79%' else 0
    attendance_40_59 = 1 if attendance == '40%-59%' else 0
    attendance_below_40 = 1 if attendance == 'Below 40%' else 0

    semester = st.number_input('Semester', min_value=1, max_value=12, value=1, step=1)
 
    # Menampilkan Input yang Dipilih
    with st.expander("Rangkuman Data Anda"):
        result = {
            'Last GPA': last_gpa,
            'Preparation': preparation,
            'Attendance': attendance,
            'Semester': semester
        }
        st.write(result)

    # Prediksi Status
    if st.button("Prediksi Status"):
        prediksi = predict_status(last_gpa, preparation_0_1_hour, preparation_2_3_hours, preparation_more_than_3_hours, 
                                 attendance_80_100, attendance_60_79, attendance_40_59, attendance_below_40, semester)
        if prediksi != "Error":
            st.success(f"Prediksi Status: **{prediksi}**")

if __name__ == '__main__':
    run_ml_app()
