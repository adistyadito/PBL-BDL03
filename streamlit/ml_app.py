import streamlit as st
import joblib
import os

# Fungsi Prediksi dengan Model ML
def predict_status(last_gpa, preparation_0_1_hour, preparation_2_3_hours, preparation_more_than_3_hours, 
                   attendance_80_100, attendance_60_79, attendance_40_59, attendance_below_40, semester):
    # Load Model
    model_path = 'student_mod.pkl'
    if not os.path.exists(model_path):
        st.error("Model tidak ditemukan! Harap tambahkan model yang valid.")
        return "Error"

    model = joblib.load(model_path)

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