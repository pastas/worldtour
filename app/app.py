import base64
import os

import folium
import numpy as np
import panel as pn
from folium import IFrame

pn.extension(sizing_mode="stretch_width")

m = folium.Map(zoom_start=12)
folium_pane = pn.pane.plot.Folium(m, height=500, sizing_mode="stretch_width")

dir = "./img/"
for fl in os.listdir(dir):
    if fl.endswith(".png"):
        idx = str(fl.split(".")[0])
        encoded = base64.b64encode(open("./img/{}.png".format(idx), "rb").read())
        html = '<img src="data:image/png;base64,{}" width="500px">'.format
        iframe = IFrame(html(encoded.decode("UTF-8")), width=500, height=380)
        popup = folium.Popup(iframe, max_width=500)

        folium.Marker(
            location=[47 + np.random.rand(1) * 0.5, 10 + np.random.rand(1) * 10],
            popup=popup,
            icon=folium.Icon(),
            color="#009BE0",
        ).add_to(m)
    else:
        continue
m.add_child(folium.LatLngPopup())

text = """
Welcome to the Pastas model demo website, showing the locations of the Pastas models
around the world. Click on the markers to see the Pastas model and more information on
the Pastas application.

Want to add a model? Send a pas-file of a models you want to add to us by submitting an
issue on <a href="https://github.com/pastas/worldtour/issues">Github</a>.
"""

left = pn.Column(
    "# Welcome!",
    pn.layout.Divider(),
    text,
    styles=dict(background="whitesmoke"),
)

png_pane = pn.pane.PNG("app/img/logo_small.png")

template = pn.template.BootstrapTemplate(
    title="Pastas around the world",
    sidebar=[left, png_pane],
    main_max_width="100%",
    main=[folium_pane],
    header_background="#009BE0",
    favicon="app/img/favo.ico",

)

# Save as a standalone HTML file
template.servable()
template.save("index.html", )