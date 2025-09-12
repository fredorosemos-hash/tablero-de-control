import pandas as pd
import streamlit as st


st.set_page_config(page_title="DASHBOARD DE DELITOS - FISCALIA", layout="centered")
st.header("DASHBOARD DE DELITOS - FISCALIA")

url = "https://github.com/juliandariogiraldoocampo/ia_taltech/raw/refs/heads/main/fiscalia/datos_generales_ficticios.csv"

df = pd.read_csv(url, sep=';', encoding= 'utf-8')

st.title('Datos Generales Ficticios')
st.dataframe(df)

seleccion_columnas = ['FECHA_HECHOS', 'DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
df = df[seleccion_columnas].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)

df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')

df_serie_tiempo = df.copy()
df_serie_tiempo['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

# CONSTRUIR LA PAGINA

st.set_page_config(page_title="Dasboard de Delitos - Fiscalia", layout="centered")
st.header("Dasborard de Delitos  - Fiscalia")
st.dataframe(df)

#st.markdown(f"<h3>Municipios con más delitos: {max_municipio}</h3>", unsafe_allow_html=True)
#st.markdown(f"<h3>Cantidad de Delitos: {max_cantidad_delitos}</h3>", unsafe_allow_html=True)

st.subheader("Tipo de Delito")
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)

max_municipio = df['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
st.write(f'Municipio TOP Delitos: {max_municipio}')


#st.dataframe(df)
#st.write(f"### MUNICPIO CON MAS DELITOS : {max_municipio} con {max_cantidad_municipio} reportes")