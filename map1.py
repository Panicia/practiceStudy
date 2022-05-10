#from urllib.request import urlopen
#import json
#with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    #counties = json.load(response)

import pandas as pd
#df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   #dtype={"fips": str})

import plotly.express as px

from parceVac import parceVac as pV
from parceGeo import myGeom as pG

pv = pV()
pv.parceAll()
pg = pG()
pg.parceAll()

names = pv.getDatalistFromAll('iso_code', 'end')
attributes = pv.getDatalistFromAll('people_vaccinated', 'end')

dP = {'names': names, 'attr': attributes}

for i in range(0, len(pg.counties) - 1):
    for j in range(0, len(names) - 1):
        if names[j] == pg.counties['features'][i]['id']:
            pg.counties['features'][i]['properties']['attribute'] = attributes[j]
            break

jF = pg.counties
dF = pd.DataFrame(data = dP)


fig = px.choropleth_mapbox(dF, geojson = jF, locations = 'names', color = 'attr',
                           color_continuous_scale="Viridis",
                           range_color=(0, 100000000),
                           mapbox_style="carto-positron",
                           zoom=1, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'attr':'covid'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()