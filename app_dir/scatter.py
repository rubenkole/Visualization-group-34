from bokeh.models import Select
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.models.widgets import Div
from bokeh.layouts import layout
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import pandas as pd
from os.path import dirname, join


df = pd.read_excel("dataset/Quantitative.xlsx")
quantitative_columns = df.columns.to_list()
edited_quantitative_columns = quantitative_columns[1:]


def Converter(cols):
    l = []
    for n, j in enumerate(cols):
        l.append(cols[n])
        l.append(j)
    outRes = dict((l[i], l[i]) if i < len(l) else (l[i], '') for i in range(len(l)))
    return outRes


cols = Converter(edited_quantitative_columns)


source = ColumnDataSource(data=dict(x=[], y=[]))

p = figure(plot_height=600, plot_width=700, title="", toolbar_location="right", sizing_mode="scale_both")
p.circle(x="x", y="y", source=source, size=7, color="blue")


def update():
    global title_name
    df = pd.read_excel("dataset/Quantitative.xlsx")
    x_name = cols[x_axis.value]
    y_name = cols[y_axis.value]

    p.xaxis.axis_label = x_axis.value
    p.yaxis.axis_label = y_axis.value

    source.data = dict(
        x=df[x_name],
        y=df[y_name]
    )





x_axis = Select(title="X-axis", options=sorted(cols.keys()), value="Serum Glucose")
y_axis = Select(title="Y-axis", options=sorted(cols.keys()), value="Hemoglobin")

controls = [x_axis, y_axis]
for control in controls:
    control.on_change('value', lambda attr, old, new: update())

heading = Div(text=open(join(dirname(__file__), "heading.html")).read(), sizing_mode="stretch_width")

update()

inputs = column(*controls, width=320, height=1000)
inputs.sizing_mode = "fixed"

layout = layout([
    [heading],
    [inputs, p],
])
curdoc().add_root(layout)
