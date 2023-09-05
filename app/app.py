import panel as pn
import hvplot.pandas
import folium
import os
import base64
from folium import IFrame
import numpy as np


pn.extension(sizing_mode="stretch_width")

m = folium.Map(zoom_start=12, max_bounds=True)

folium_pane = pn.pane.plot.Folium(m, height=500)

dir = "./img/"
for fl in os.listdir(dir):
    if fl.endswith(".png"):
        idx = str(fl.split(".")[0])
        encoded = base64.b64encode(open("./img/{}.png".format(idx), "rb").read())
        html = '<img src="data:image/png;base64,{}">'.format
        iframe = IFrame(html(encoded.decode("UTF-8")), width=630, height=380)
        popup = folium.Popup(iframe, max_width=1000)

        folium.Marker(
            location=[50 + np.random.rand(1) * 10, 10 + np.random.rand(1) * 100],
            popup=popup,
            icon=folium.Icon(),
        ).add_to(m)
    else:
        continue
m.add_child(folium.LatLngPopup())


template = pn.template.BootstrapTemplate(
    title="Pastas around the world",
    sidebar=[],
)
# Append a layout to the main area, to demonstrate the list-like API
template.main.append(pn.Row(folium_pane))

# template.servable()

from bokeh.resources import INLINE

template.save("index.html", resources=INLINE)
