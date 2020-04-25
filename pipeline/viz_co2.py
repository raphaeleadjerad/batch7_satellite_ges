import folium
import webbrowser
import pandas as pd
import math
from folium import Marker
from folium.plugins import HeatMap, MarkerCluster


df = pd.read_csv("dataset/CO2_emissions_Edgar_2017_v3.csv")
df["CO2 classification"].value_counts()
co2 = df.loc[df["CO2 classification"] == 4, :].copy()
centrales = pd.read_csv("dataset/CO2_emissions_centrale.csv")
centrales = centrales.loc[:, ["latitude", "longitude", "tCO2_emitted_in_2017",
                              "tCO2_emitted_in_2017_with estimated_data"]].copy()

m_1 = folium.Map(location=[48.85, 2.35], tiles='stamentoner', zoom_start=2)

HeatMap(data=co2[['latitude', 'longitude', 'CO2 emissions']], radius=1,
        blur=1, gradient={1: 'red'}).add_to(m_1)

mc = MarkerCluster()
for idx, row in centrales.iterrows():
    if not math.isnan(row['latitude']) and not math.isnan(row['longitude']):
        mc.add_child(Marker([row['latitude'], row['longitude']]))
m_1.add_child(mc)

m_1.save('mymap.html')
webbrowser.open('mymap.html', new=2)
