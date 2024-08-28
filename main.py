import streamlit as st
import pandas as pd
from docx import Document
from docx.shared import Inches
import matplotlib.pyplot as plt
import io

def main():
    st.title('Generador de Informes desde Plantillas')
    template_file = st.file_uploader('Cargar plantilla de Word', type='docx')
    data_file = st.file_uploader('Cargar datos Excel o csv', type=['xlsx', 'csv'])
    if template_file and data_file:
        st.success('Archivos cargados correctamente')
        df = pd.read_csv(data_file) if data_file.name.endswith('.csv') else pd.read_excel(data_file)
        st.subheader('Datos cargados')
        st.dataframe(df)

main()
