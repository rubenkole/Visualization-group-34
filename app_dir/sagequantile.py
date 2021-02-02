from bokeh.io import curdoc
from bokeh.models.widgets import Div
from bokeh.layouts import layout
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.models import Button
from bokeh.models.widgets import Div
from bokeh.layouts import layout

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
import numpy as np
from bokeh.io import output_notebook
from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap
import pandas as pd

from bokeh.io import show
from bokeh.models import CustomJS, RadioButtonGroup
import os
import sys
import webbrowser
from os.path import dirname, join
import pickle
import pandas as pd
from bokeh.models.tools import HoverTool


af = pd.read_excel("dataset/agequantile.xlsx")
grouped = af.groupby('Unnamed: 0')['positive','negative'].sum()

df  = ColumnDataSource(grouped)
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