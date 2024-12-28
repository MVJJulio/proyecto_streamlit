import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la página
st.title("Análisis de Hipótesis")

# Cargar el dataset
ruta_dataset = 'data/Sample - Superstore.csv'

try:
    df = pd.read_csv(ruta_dataset)

    # Hipótesis 1: El envío se realiza mayormente en la clase estándar
    st.subheader("Hipótesis 1: El envío se realiza mayormente en la clase estándar")
    ship_mode_conteo = df['Ship Mode'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.bar(ship_mode_conteo.index, ship_mode_conteo.values, color='skyblue')
    ax1.set_title("Conteo de Ship Modes")
    ax1.set_xlabel("Ship Mode")
    ax1.set_ylabel("Cantidad")
    st.pyplot(fig1)

    # Hipótesis 2: Las ciudades de Los Ángeles y Nueva York tienen más pedidos
    st.subheader("Hipótesis 2: Las ciudades de Los Ángeles y Nueva York tienen más pedidos")
    top_10_ciudades = df['City'].value_counts().head(10)
    fig2, ax2 = plt.subplots()
    ax2.bar(top_10_ciudades.index, top_10_ciudades.values, color='teal')
    ax2.set_title("Top 10 Ciudades con Más Pedidos")
    ax2.set_xlabel("Ciudad")
    ax2.set_ylabel("Cantidad de Pedidos")
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

    # Hipótesis 3: Para Home Office es donde menos pedidos se realizan
    st.subheader("Hipótesis 3: Para Home Office es donde menos pedidos se realizan")
    conteo_segmentos = df['Segment'].value_counts()
    fig3, ax3 = plt.subplots()
    ax3.bar(conteo_segmentos.index, conteo_segmentos.values, color=['teal', 'orange', 'purple'])
    ax3.set_title("Cantidad de Pedidos por Segmento")
    ax3.set_xlabel("Segmento")
    ax3.set_ylabel("Cantidad de Pedidos")
    st.pyplot(fig3)

    # Hipótesis 4: Las órdenes en ciudades principales tienen un valor promedio de venta más alto
    st.subheader("Hipótesis 4: Las órdenes en ciudades principales tienen un valor promedio de venta más alto")
    ciudades_principales = ['New York City', 'Los Angeles']
    df['is_principal'] = df['City'].isin(ciudades_principales)
    promedio_principales = df[df['is_principal']]['Sales'].mean()
    promedio_otras = df[~df['is_principal']]['Sales'].mean()
    fig4, ax4 = plt.subplots()
    ax4.bar(['Ciudades Principales', 'Otras Ciudades'], [promedio_principales, promedio_otras], color=['blue', 'gray'])
    ax4.set_title("Promedio de Ventas: Ciudades Principales vs Otras Ciudades")
    ax4.set_ylabel("Promedio de Ventas")
    st.pyplot(fig4)

    # Hipótesis 5: Valor promedio de ventas para diferentes métodos de envío
    st.subheader("Hipótesis 5: Valor promedio de ventas para diferentes métodos de envío")
    promedio_envio = df.groupby('Ship Mode')['Sales'].mean()
    fig5, ax5 = plt.subplots()
    ax5.bar(promedio_envio.index, promedio_envio.values, color='green')
    ax5.set_title("Promedio de Ventas por Método de Envío")
    ax5.set_xlabel("Método de Envío")
    ax5.set_ylabel("Promedio de Ventas")
    st.pyplot(fig5)

except FileNotFoundError:
    st.error(f"No se encontró el archivo en la ruta: {ruta_dataset}")
except Exception as e:
    st.error(f"Ha ocurrido un error: {str(e)}")
