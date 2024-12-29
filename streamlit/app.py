import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
from ml_app import run_ml_app
from dashboard import run_dashboard


def main():
    menu = ['Dashboard', 'Machine Learning']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Dashboard':
        st.subheader('Dashboard Performa Mahasiswa')
        run_dashboard()
    elif choice == 'Machine Learning':
        st.subheader('Analisis Status Mahasiswa')
        run_ml_app()


if __name__ == '__main__':
    main()
