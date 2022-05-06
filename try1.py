import plotly.graph_objects as go
from parceVac import parseVac as pV

pv = pV('vaccinations.txt')
pv.parseAll()



fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3], x=[4,5,6])],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show()