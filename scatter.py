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

from bokeh.io import show
from bokeh.models import CustomJS, RadioButtonGroup
import os
import sys


df = pd.read_excel("dataset/Quantitative.xlsx")
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


source = ColumnDataSource(data=dict(x=[], y=[]))




p = figure(plot_height=600, plot_width=700, title="", toolbar_location="right", sizing_mode="scale_both")
p.circle(x="x", y="y",source = source,size = 7,color = "blue")

def dataset():
    if radio_button_group.active == 0:

        print("Categorical")
        os.system("bokeh serve sagequantile.py --show --port 5007")
    elif radio_button_group.active == 1:

        print("Quantitative")

    else:
        print("Age quantile")


def update():
    df = pd.read_excel("dataset/Quantitative.xlsx")
    x_name = cols[x_axis.value]
    y_name = cols[y_axis.value]

    p.xaxis.axis_label = x_axis.value
    p.yaxis.axis_label = y_axis.value

    source.data = dict(
        x=df[x_name],
        y=df[y_name]
    )


x_axis = Select(title="X-axis",options=sorted(cols.keys()),value="Serum Glucose")
y_axis = Select(title="Y-axis",options=sorted(cols.keys()),value="Hemoglobin")
radio_button_group = RadioButtonGroup(labels=["Categorical","Quantitative","Age Quantile"],active=1)
radio_button_group.on_change('active',lambda attr, old, new: dataset())

controls = [x_axis, y_axis]
for control in controls:
    control.on_change('value', lambda attr, old, new: update())

heading = Div(text = "<b>test!</b>", style={'font-size': '200%', 'color': 'blue','text-align':'center'})


update()
dataset()

layout = layout(heading, column(radio_button_group,x_axis,y_axis),p)
curdoc().add_root(layout)