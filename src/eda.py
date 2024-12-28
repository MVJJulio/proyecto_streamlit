import pandas as pd

def cargar_datos(ruta):
    """
    Carga el dataset desde un archivo CSV.
    """
    return pd.read_csv(ruta)

def primeras_filas(df, n=5):
    """
    Devuelve las primeras filas del DataFrame.
    """
    return df.head(n)

def informacion_general(df):
    """
    Devuelve información general del DataFrame.
    """
    return df.info()

def valores_nulos(df):
    """
    Devuelve la cantidad de valores nulos por columna.
    """
    return df.isnull().sum()

def valores_unicos(df):
    """
    Devuelve la cantidad de valores únicos por columna.
    """
    return {col: df[col].nunique() for col in df.columns}

def resumen_estadistico(df):
    """
    Devuelve el resumen estadístico de las columnas numéricas.
    """
    return df.describe()

