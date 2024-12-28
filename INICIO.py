import streamlit as st

st.title("INICIO")
st.subheader("Proyecto Streamlit")
st.subheader("Bienvenido")
# Descripción
st.markdown(
    """
    Este proyecto incluye las siguientes páginas:
    """
)

# Contenido con imagen y texto
col1, col2 = st.columns([1, 3])

with col1:
    # Imagen
    st.image("utils/eda_icon.png", width=150)  # Asegúrate de reemplazar "eda_icon.png" con el nombre de tu imagen.

with col2:
    # Título y descripción
    st.markdown(
        """
        ### EDA: Análisis exploratorio de datos
        Examina los datos y descubre patrones interesantes.
        """
    )
    
col1, col2 = st.columns([1, 3])

with col1:
    # Imagen
    st.image("utils/hipotesis.png", width=150)  # Asegúrate de reemplazar "eda_icon.png" con el nombre de tu imagen.

with col2:
    # Título y descripción
    st.markdown(
        """
        ### Hipótesis: Visualización de hipótesis propuestas
        Evalúa diferentes hipótesis mediante gráficos interactivos.
        """
    )
col1, col2 = st.columns([1, 3])

with col1:
    # Imagen
    st.image("utils/modelo.png", width=150)  # Asegúrate de reemplazar "eda_icon.png" con el nombre de tu imagen.

with col2:
    # Título y descripción
    st.markdown(
        """
        ###  Modelo: Predicciones con un modelo de árbol de decisiones
        Genera predicciones y evalúa el desempeño del modelo.
        """
    )