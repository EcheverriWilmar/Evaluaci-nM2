import streamlit as st
import pandas as pd

df = pd.read_csv('historico_resultados_pruebas_saber_11.csv')

st.title('Visualización de los que sacaron puntaje mayor a 40 en matematicas')

def mayor30(puntaje_matematicas):
    return puntaje_matematicas > 40

filtro_mayor30 = df[mayor30(df["puntaje_matematicas"])]
st.write(filtro_mayor30)

st.title('Visualización de los que sacaron puntaje mayor general a 40 en Medellin')

def mayor30cien(punt_global_med):
    return punt_global_med > 40

filtro_mayor30cien = df[mayor30cien(df["punt_global_med"])]
st.write(filtro_mayor30cien)

st.title('Filtro de Datos por Establecimiento')

selec_esta = st.selectbox('Seleccione Establecimiento', df['establecimiento'].unique())

filtro_esta = df[df['establecimiento'] == selec_esta]
st.write(filtro_esta)

st.title('El puntaje maryor general')

indice_maximo = df['puntaje_global'].idxmax()

  
fila_maxima = df.loc[indice_maximo]

st.write(fila_maxima)

st.title('El puntaje Menor general')
indice_minimo = df['puntaje_global'].idxmin()

   
fila_minima = df.loc[indice_minimo]

st.write(fila_minima)