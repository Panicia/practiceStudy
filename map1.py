import pandas as pd
import plotly.express as px

from parceVac import parceVac as pV
from fionaTest import fionaTests as pG

pv = pV()
pg = pG()

names = pv.getDatalistFromAll('location', 'end')
attributes = pv.getDatalistFromAll('people_vaccinated', 'end')
#names = pv.data['iso_code']
#attributes = pv.data['people_vaccinated']

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