import pandas as pd
import plotly.express as px

df = pd.read_csv("mapas_mexico.csv")

# 2. Creamos el mapa interactivo
# Usamos scatter_mapbox para poner puntos en un mapa
fig = px.scatter_mapbox(
    df, 
    lat="Latitud", 
    lon="Longitud", 
    hover_name="Ciudad",          # Texto que aparece al pasar el ratón
    hover_data=["Estado"],        # Información extra al pasar el ratón
    size="Ventas_Anuales",        # El tamaño del círculo depende de las ventas
    color="Ventas_Anuales",       # El color también cambia según las ventas
    color_continuous_scale=px.colors.cyclical.IceFire, # Paleta de colores
    size_max=30,                  # Tamaño máximo de los círculos
    zoom=4,                       # Nivel de zoom inicial
    mapbox_style="carto-positron" # Estilo del mapa (claro y limpio)
)

# 3. Ajustamos un poco los márgenes para que se vea bien
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# 4. ¡Mostramos el mapa en el navegador!
fig.show()