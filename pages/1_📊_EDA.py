import streamlit as st
import pandas as pd
from src.eda import (
    cargar_datos,
    primeras_filas,
    valores_nulos,
    valores_unicos,
    resumen_estadistico
)

# Carga de datos
st.title("Exploración de Datos")
ruta_dataset = 'data/Sample - Superstore.csv'

try:
    data = cargar_datos(ruta_dataset)

    # Mostrar primeras filas
    st.subheader("Primeras filas del dataset:")
    st.write(primeras_filas(data))

    # Información general del dataset
    st.subheader("Información general del dataset:")
    buffer = st.empty()
    buffer.write("Nota: Streamlit no soporta directamente el método `.info()`. Consulte los logs para más detalles.")
    st.text(str(data.info()))

    # Valores nulos
    st.subheader("Valores nulos en el dataset:")
    st.write(valores_nulos(data))

    # Valores únicos
    st.subheader("Valores únicos en cada columna:")
    unicos = valores_unicos(data)
    for col, unique_count in unicos.items():
        st.write(f"{col}: {unique_count} únicos")

    # Resumen estadístico
    st.subheader("Resumen estadístico de columnas numéricas:")
    st.write(resumen_estadistico(data))

except FileNotFoundError:
    st.error(f"No se encontró el archivo en la ruta: {ruta_dataset}")

