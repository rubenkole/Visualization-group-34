from bokeh.io import curdoc
from bokeh.models.widgets import Div
from bokeh.layouts import layout
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from os.path import dirname, join
import pandas as pd
from bokeh.models.tools import HoverTool


af = pd.read_excel("dataset/agequantile.xlsx")

grouped = af.groupby('Unnamed: 0')['positive','negative'].sum()


df = ColumnDataSource(grouped)
quantiles = df.data['Unnamed: 0'].tolist()

quantiles2 = []
for _ in quantiles:
    i = str(_)
    quantiles2.append(i)

p = figure(x_range=quantiles2)

p.vbar(x="Unnamed: 0", top="positive", width=0.7, source=df)

p.title.text = 'Positive Corona Tests Per Age Quantile'
p.legend.location = 'top_left'

p.xaxis.axis_label = 'Age Quantile'
p.xgrid.grid_line_color = None  # remove the x grid lines

p.yaxis.axis_label = 'Positive Tests'

hover = HoverTool()
hover.tooltips = [
    ("Negative", "@negative")]

hover.mode = 'vline'

p.add_tools(hover)

heading = Div(text=open(join(dirname(__file__), "heading.html")).read(), sizing_mode="stretch_width")



layout = layout([
    [heading],
    [p],
])
curdoc().add_root(layout)