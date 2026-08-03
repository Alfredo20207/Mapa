import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuración de la página (Pestaña del navegador)
st.set_page_config(page_title="Dashboard de Ventas", layout="wide")

# 2. Título principal
st.title("🗺️ Dashboard Interactivo de Ventas en México")
st.markdown("Este es un proyecto para mi portafolio mostrando Pandas, Plotly y Streamlit.")

# 3. Cargar los datos
# Usamos cache para que la app sea más rápida y no lea el CSV en cada clic
@st.cache_data
def load_data():
    return pd.read_csv('mapas_mexico.csv')

df = load_data()

# 4. Crear una barra lateral (Sidebar) para los controles interactivos
st.sidebar.header("Filtros")

# Slider para filtrar por ventas
ventas_minimas = st.sidebar.slider(
    "Filtrar por Ventas Mínimas:",
    min_value=int(df["Ventas_Anuales"].min()),
    max_value=int(df["Ventas_Anuales"].max()),
    value=400 # Valor por defecto
)

# 5. Filtrar el DataFrame basado en el Slider
df_filtrado = df[df["Ventas_Anuales"] >= ventas_minimas]

# 6. Crear el diseño en 2 columnas para el mapa y los datos
col1, col2 = st.columns([2, 1]) # El mapa ocupa el doble de espacio que la tabla

with col1:
    st.subheader("Mapa Geográfico de Ventas")
    # Generamos el mapa con los datos filtrados
    fig = px.scatter_mapbox(
        df_filtrado, 
        lat="Latitud", 
        lon="Longitud", 
        hover_name="Ciudad",
        hover_data=["Estado", "Ventas_Anuales"],
        size="Ventas_Anuales",
        color="Ventas_Anuales",
        color_continuous_scale=px.colors.sequential.Plasma,
        size_max=30,
        zoom=4.5,
        mapbox_style="carto-positron"
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    # Mostramos el mapa en Streamlit
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Datos en Crudo")
    st.write(f"Mostrando {len(df_filtrado)} ciudades.")
    # Mostramos el dataframe como una tabla interactiva
    st.dataframe(df_filtrado[['Ciudad', 'Estado', 'Ventas_Anuales']], hide_index=True)