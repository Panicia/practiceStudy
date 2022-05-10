import plotly.graph_objects as go
import plotly.express as px

from parceVac import parceVac as pV

pv = pV('vaccinations.txt')
pv.parceAll()


'''name = 'people_vaccinated'
fig = go.Figure(
    data=[go.Bar(y = pv.getDatalistFromAll(name, 'end'), x = pv.getDatalistFromAll('location', 'end')), 
          go.Bar(y = pv.getDatalistFromAll(name, 'start'), x = pv.getDatalistFromAll('location', 'start'))],
    layout_title_text = name
)
fig.show()'''

df = px.data.tips()
fig = px.histogram(y = pv.getDatalistFromAll('daily_people_vaccinated_per_hundred', 'end'), x = pv.getDatalistFromAll('location', 'end'))
fig.show()

'''name = 'people_vaccinated_per_hundred'

X1 = pv.getDataListPerCountry('Latvia', 'date')
Y1 = pv.getDataListPerCountry('Latvia', name)
l1 = {'date': X1, name: Y1}

X2 = pv.getDataListPerCountry('Russia', 'date')
Y2 = pv.getDataListPerCountry('Russia', name)
l2 = {'date': X2, name: Y2}

X3 = pv.getDataListPerCountry('United States', 'date')
Y3 = pv.getDataListPerCountry('United States', name)
l3 = {'date': X3, name: Y3}

fig = go.Figure()
fig.add_trace(go.Scatter(x = X1, y = Y1,
                    mode='lines',
                    name='Latvia'))
fig.add_trace(go.Scatter(x = X2, y = Y2,
                    mode='lines',
                    name='Russia'))
fig.add_trace(go.Scatter(x = X3, y = Y3,
                    mode='lines',
                    name='United States'))

fig.show()'''