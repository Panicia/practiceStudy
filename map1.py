import pandas as pd
import plotly.express as px

from parceVac import parceVac as pV
from fionaTest import fionaTests as pG

import math

pv = pV()
pg = pG()

names = pv.getDatalistFromAll('iso_code', 'end')
attributes = pv.getDatalistFromAll('people_fully_vaccinated', 'end')

for i in range(len(attributes)):
    if math.isnan(attributes[i]):
        attributes[i] = -1

dP = {'names': names, 'attr': attributes}
jF = pg.getData()

doubles = pg.findDubles()

for i in range(len(jF['features'])):
    for j in range(len(names)):
        if names[j] == jF['features'][i]['properties']['adm0_a3']:
            jF['features'][i]['id'] = names[j]

   
for i in doubles:
    k = 0
    for id in i['id']:
        jF['features'][id]['id'] = i['name'] + str(k)
        k += 1
    for m in range(len(names)):
        if names[m] == i['name']:
            names[m] = i['name'] + "0"
            for j in range(1,i['numDoubs']):
                names.insert(m+j,i['name'] + str(j))
                attributes.insert(m+j,attributes[m])

dF = pd.DataFrame(data = dP)

'''counties = {
            'type': 'FeatureCollection',
            'features': [jF['features'][18], jF['features'][22]]
            }

rr = {'names': [jF['features'][18]['id'], jF['features'][22]['id']], 'attr': [1,2]}            
kek = pd.DataFrame(data = rr)'''

fig = px.choropleth_mapbox(dP, geojson = jF, locations = 'names', color = 'attr',
                           color_continuous_scale="Viridis",
                           range_color=(0, 100000000),
                           mapbox_style="carto-positron",
                           zoom=1, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'attr':'covid'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()