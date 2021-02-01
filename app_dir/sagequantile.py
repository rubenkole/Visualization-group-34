from bokeh.io import curdoc
from bokeh.models.widgets import Div
from bokeh.layouts import layout


heading = Div(text = "<b>This is a placeholder for the Age Quantile Graph</b>", style={'font-size': '200%', 'color': 'blue','text-align':'center'})


layout = layout(heading)
curdoc().add_root(layout)
