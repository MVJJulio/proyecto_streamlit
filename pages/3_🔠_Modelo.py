import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Título de la página
st.title("Modelo de Regresión Lineal")

# Cargar el dataset
ruta_dataset = 'data/Sample - Superstore.csv'

try:
    data = pd.read_csv(ruta_dataset)

    # Selección de características y variable objetivo
    st.subheader("Preparación de datos")
    features = ['Sales', 'Quantity', 'Discount', 'Ship Mode', 'Segment', 'Category', 'Sub-Category']
    target = 'Profit'

    st.write("Características seleccionadas para el modelo:", features)
    st.write("Variable objetivo:", target)

    # Codificación de variables categóricas
    data_encoded = pd.get_dummies(data[features], columns=['Ship Mode', 'Segment', 'Category', 'Sub-Category'], drop_first=True)

    # División en conjuntos de entrenamiento y prueba
    X = data_encoded
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenamiento del modelo
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predicción y evaluación del modelo
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Mostrar métricas de evaluación
    st.subheader("Evaluación del Modelo")
    st.write(f"- **Error Cuadrático Medio (MSE):** {mse:.2f}")
    st.write(f"- **Coeficiente de Determinación (R²):** {r2:.2f}")

    # Análisis de correlación
    st.subheader("Análisis de Correlación")
    correlation = data[['Sales', 'Quantity', 'Discount', 'Profit']].corr()

    # Visualización del mapa de calor
    st.write("**Mapa de calor de correlación:**")
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax1)
    st.pyplot(fig1)

    # Gráfico de dispersión: Sales vs Profit
    st.subheader("Relación entre Ventas y Ganancia")
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='Sales', y='Profit', data=data, ax=ax2)
    ax2.set_title("Relación entre Sales y Profit")
    ax2.set_xlabel("Sales")
    ax2.set_ylabel("Profit")
    st.pyplot(fig2)

except FileNotFoundError:
    st.error(f"No se encontró el archivo en la ruta: {ruta_dataset}")
except Exception as e:
    st.error(f"Ha ocurrido un error: {str(e)}")
