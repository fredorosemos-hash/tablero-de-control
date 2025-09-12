import pandas as pd
import streamlit as st
import plotly.express as px

url = 'https://github.com/juliandariogiraldoocampo/ia_taltech/raw/refs/heads/main/fiscalia/datos_generales_ficticios.csv'
df = pd.read_csv(url, sep=';', encoding='utf-8')

# Crear lista de las Columnas de Interés
seleccion_columnas = ['FECHA_HECHOS','DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
# Actualizo el dataframe -df- con las columnas de interés, ordenadas por fecha y reseteo el índice
df = df[seleccion_columnas].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)

# Convierto la columna FECHA_HECHOS a formato fecha
df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')
# Extraigo solo la fecha (sin hora)
df['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

conteo_municipios = df['MUNICIPIO_HECHOS'].value_counts()

# CÁLCULO DE MUNICIPIO CON MAS DELITOS
max_municipio = df['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
max_cantidad_municipio = df['MUNICIPIO_HECHOS'].value_counts().iloc[0]

# CALCULO DE LA ETAPA QUE MAS VECES SE PRESENTA
# Ya que value_counts() genera un dataframe ORDENADO, traigo solo EL PRIMER INDICE .index[0]
etapa_mas_frecuente = df['ETAPA'].value_counts().index[0].upper()
# Ya que value_counts() genera un dataframe ORDENADO, traigo solo EL PRIMER VALOR .iloc[0]
cant_etapa_mas_frecuente = df['ETAPA'].value_counts().iloc[0]

# CONSTRUIR LA PÁGINA
st.set_page_config(page_title="Dashboard de Delitos - Fiscalía", layout="centered")
st.title("Dashboard de Delitos - Fiscalía")

st.dataframe(df)

st.subheader(f"Municipio con más delitos: {max_municipio} con {max_cantidad_municipio} reportes")
st.subheader(f'{etapa_mas_frecuente} tiene {cant_etapa_mas_frecuente} registros')

st.subheader('Comportamiento Delitos')
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)

st.subheader('Departamentos con mas Casos')
departamento = df['DEPARTAMENTO'].value_counts()
st.bar_chart(departamento)

st.subheader("Distribución por Departamentos")
fig = px.pie(
	names=departamento.index,  # Para los nombres de la Torta
	values=departamento.values # Para los valores de la Torta
)
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.update_layout(showlegend=False, height=400)
st.plotly_chart(fig)

df_delitos = df.groupby(['DEPARTAMENTO', 'DELITO']).size().reset_index(name='conteo')
fig = px.bar(df_delitos, x='DEPARTAMENTO', y='conteo', color='DELITO', barmode='stack')
st.plotly_chart(fig)
st.write(df_delitos)
