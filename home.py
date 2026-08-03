import pandas as pd
import folium

df = pd.read_csv('practica_casa.csv')

centro_lat = df['Latitude'].mean()
centro_lon = df['Longitude'].mean()

fuente_satelital = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
creditos = 'Tiles © Esri — Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'

mapa = folium.Map(
    location=[centro_lat, centro_lon], 
    zoom_start=14,
    tiles=fuente_satelital,
    attr=creditos
)

puntos_ruta = list(zip(df['Latitude'], df['Longitude']))

folium.PolyLine(puntos_ruta, color="blue", weight=4, opacity=0.8).add_to(mapa)

folium.Marker(puntos_ruta[0], popup='Inicio', icon=folium.Icon(color='green')).add_to(mapa)
folium.Marker(puntos_ruta[-1], popup='Fin', icon=folium.Icon(color='red')).add_to(mapa)

mapa.save('mapa_gps.html')
print("¡Listo! El mapa se ha guardado como 'mapa_gps.html'")