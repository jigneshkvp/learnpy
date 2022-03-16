from textwrap import fill
from turtle import color, fillcolor, st
import folium
import pandas


def get_elev_color(el):
    if el < 1500:
        return "green"
    elif 1500 <= el < 2500:
        return "orange"
    else:
        return "red"


data = pandas.read_csv("volcanoes.csv")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

base_loc = [42.77619196211615, -109.86460522620602]

# base map
map = folium.Map(location=base_loc, zoom_start=5, tiles="cartodbpositron")

# feature group - Population
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(
    folium.GeoJson(
        data=open("world.json", "r", encoding="utf-8-sig").read(),
        style_function=lambda x: {
            "fillColor": "green"
            if x["properties"]["POP2005"] < 10000000
            else "orange"
            if 10000000 <= x["properties"]["POP2005"] < 20000000
            else "red"
        },
    )
)

# defaultfeature group - Volcanoes
fgv = folium.FeatureGroup(name="Volcanoes")
# marker
for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=75)
    # marker = folium.Marker(
    #     location=[lt, ln],
    #     popup=folium.Popup(iframe),
    #     icon=folium.Icon(color=get_elev_color(el)),
    # )
    marker = folium.CircleMarker(
        location=[lt, ln],
        radius=6,
        popup=folium.Popup(iframe),
        color="grey",
        fill=True,
        fill_color=get_elev_color(el),
        fill_opacity=0.7,
    )
    fgv.add_child(marker)


# add the feature group with marker to the map
map.add_child(fgv)
map.add_child(fgp)

# add layer control
map.add_child(folium.LayerControl())

# save the map
map.save("map1.html")
