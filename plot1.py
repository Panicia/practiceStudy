import plotly.graph_objects as go
import plotly.express as px

from parceVac import parceVac as pV

pv = pV()

def plotData(countries, name):
    fig = go.Figure()
    
    for c in countries:
        X = pv.getDataListPerCountry(c, 'date')
        Y = pv.getDataListPerCountry(c, name)
        fig.add_trace(go.Scatter(x = X, y = Y,
                                    mode='lines',
                                    name=c))
    fig.update_layout(
    title = name,
    xaxis_title = "Date",
    yaxis_title = name,
    legend_title = "Legend",
    font = dict(
        family="Courier New, monospace",
        size=18,
        color="Black"
    ))
    fig.show()


""" name = 'people_vaccinated'
fig = go.Figure(
                data=[go.Bar(y = pv.getDatalistFromAll(name, 'end'), x = pv.getDatalistFromAll('country', 'end'))],
                layout_title_text = name
               )
fig.show() """

""" df = px.data.tips()
fig = px.histogram(y = pv.getDatalistFromAll('people_vaccinated_per_hundred', 'end'), x = pv.getDatalistFromAll('country', 'end'))
fig.show() """

name = 'people_fully_vaccinated_per_hundred'
name1 = 'daily_vaccinations'
name2 = 'total_vaccinations'
name3 = 'total_vaccinations_per_hundred'
name4 = 'people_vaccinated'

countries = [   
                'Canada',
                'United Kingdom',
                'Latvia',
                'Russia',
                'United States',
                'Switzerland',
                'India',
                'China'
            ]

plotData(countries, name4)