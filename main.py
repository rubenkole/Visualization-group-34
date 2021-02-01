from bokeh.models.widgets import Button
from bokeh.io import curdoc

from random import random
import pandas as pd
from bokeh.layouts import column
from bokeh.plotting import figure, curdoc
from bokeh.models import RadioButtonGroup, Select
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
import webbrowser


from bokeh.io import show
from bokeh.models import CustomJS, RadioButtonGroup
import os
import sys


df = pd.read_excel("dataset/Categorical.xlsx")
cols = df.columns.to_list()
cols = cols[1:]

def Converter(cols):
    l = []
    for n, j in enumerate(cols):
        l.append(cols[n])
        l.append(j)
    outRes = dict((l[i], l[i]) if i  < len(l) else (l[i], '') for i in range(len(l)))
    return outRes


cols = Converter(cols)

source = ColumnDataSource(df)

my_dict = df[str("Influenza A")].value_counts().to_dict()
key = list(my_dict.keys())
value = list(my_dict.values())

source = ColumnDataSource(data=dict(x=key, y=value))
print(source.data["x"])



p = figure(x_range=source.data["x"])
p.vbar(x="x",top="y",width =0.9, source = source)

def dataset():
    if radio_button_group.active == 0:

        print("Categorical")

    elif radio_button_group.active == 1:

        print("Quantitative")
        webbrowser.open('http://localhost:5006/scatter')

    else:
        print("Age quantile")
        webbrowser.open('http://localhost:5006/sagequantile')

def update():
    df = pd.read_excel("dataset/Categorical.xlsx")

    my_dict = df[str(x_axis.value)].value_counts().to_dict()
    key = list(my_dict.keys())
    value = list(my_dict.values())

    source.data = dict(
        x=key,
        y=value
    )


x_axis = Select(title="Option:",options=sorted(cols.keys()),value="Influenza A")
x_axis.on_change('value', lambda attr, old, new: update())

radio_button_group = RadioButtonGroup(labels=["Categorical","Quantitative","Age Quantile"],active=0)
radio_button_group.on_change('active',lambda attr, old, new: dataset())



heading = Div(text = "<b>An interactive explorer of COVID-19 data</b>", style={'font-size': '200%', 'color': 'blue','text-align':'center'})


update()
dataset()

layout = layout(heading, column(radio_button_group,x_axis),p)
curdoc().add_root(layout)