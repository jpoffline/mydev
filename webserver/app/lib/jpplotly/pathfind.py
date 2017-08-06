import plotly
from plotly.graph_objs import Scatter, Layout

div = plotly.offline.plot({
    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world")
}, output_type="div", include_plotlyjs=False)

print div