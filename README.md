# 🎓 Prediksi Dropout Mahasiswa dengan Relational Database & Machine Learning

![Dropout Prediction](https://cdn.discordapp.com/attachments/697322005493448736/1336395592770785340/PPT_PBL_Page_01.png?ex=67a3a6e2&is=67a25562&hm=37b11de0c09ce8a32a56faed2c658d657ccf01a985728a2834d53a82984c3f00&)

## 🔍 Overview
Proyek ini bertujuan untuk **memprediksi kemungkinan mahasiswa dropout** menggunakan **Relational Database (SQL) & Machine Learning**. Dengan mengolah data mahasiswa dan menerapkan **algoritma prediksi seperti Logistic Regression & Random Forest**, model ini dapat mengidentifikasi mahasiswa yang berisiko **dropout**, **berisiko**, atau **aman**.

## 📊 Dataset
- **Sumber Data:** Dataset dari **[Mendeley](https://data.mendeley.com/datasets/5b82ytz489/1?form=MG0AV3)**  
- **Jumlah Observasi:** 493  
- **Jumlah Variabel:** 18  
- **Variabel Kunci:**  
  - `Last` (IPK Semester Terakhir)  
  - `Overall` (IPK Rata-rata)  
  - `Semester` (Tingkat semester mahasiswa)  
  - `Preparation` (Durasi persiapan belajar)  
  - `Attendance` (Tingkat kehadiran)  

## 🛠️ Metode & Tools
- **Metode:**
  - **Data Preprocessing**: Handling outliers dengan **IQR & Winsorization**
  - **Feature Engineering**: Normalisasi bobot variabel untuk prediksi  
  - **Modeling**:  
    - Logistic Regression  
    - **Random Forest dengan SMOTE (oversampling)**  

- **Tools & Libraries:**
  - 🐍 **Python (Google Colab)**
  - 📦 Pandas, NumPy, Matplotlib, Seaborn
  - 🤖 Scikit-learn (Logistic Regression, Random Forest, SMOTE)
  - 🗄️ **SQL (Relational Database)**
  - 🌐 **Streamlit (Dashboard Prediksi)**  

## 📌 Hasil Analisis
- **Model terbaik:** **Random Forest dengan SMOTE**  
- **Akurasi Model:**
  - Logistic Regression: **95.9%**
  - Random Forest: **100% (pada dataset uji)**
- **F1-Score untuk setiap kategori:** **1.00**
- **Feature paling berpengaruh:**  
  - **Last (IPK terakhir)** memiliki impact terbesar dalam prediksi dropout  

## 🎛️ Web App Demo
🎥 **Cek Model di Streamlit** 👉 [Prediksi Dropout](https://bdl888gacor.streamlit.app/)  

