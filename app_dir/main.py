
from bokeh.models import Select, FactorRange
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.models.widgets import Div
from bokeh.layouts import layout
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import pandas as pd
from os.path import dirname, join

df = pd.read_excel("dataset/Categorical.xlsx")
cols = df.columns.to_list()
cols = cols[1:]


def Converter(cols):
    l = []
    for n, j in enumerate(cols):
        l.append(cols[n])
        l.append(j)
    outRes = dict((l[i], l[i]) if i < len(l) else (l[i], '') for i in range(len(l)))
    return outRes


cols = Converter(cols)
print(cols)
source = ColumnDataSource(df)

my_dict = df[str("Influenza A")].value_counts().to_dict()
k = list(my_dict.keys())
key = [str(_) for _ in k]
value = list(my_dict.values())

source = ColumnDataSource(data=dict(x=key, y=value))

p = figure(x_range=FactorRange(factors=list(source.data['x'])))

p.vbar(x="x", top="y", width=0.7, source=source)



def update():
    df = pd.read_excel("dataset/Categorical.xlsx")

    my_dict = df[str(x_axis.value)].value_counts().to_dict()
    k = list(my_dict.keys())
    key = [str(_) for _ in k]

    value = list(my_dict.values())

    source.data = dict(
        x=key,
        y=value
    )
    p.x_range.factors = list(source.data['x'])


x_axis = Select(title="Please select a feature: ", options=sorted(cols.keys()), value="Influenza A")


controls = [x_axis]
for control in controls:
    x_axis.on_change('value', lambda attr, old, new: update())


heading = Div(text=open(join(dirname(__file__), "heading.html")).read(), sizing_mode="stretch_width")

update()


inputs = column(*controls, width=320, height=1000)
inputs.sizing_mode = "fixed"

layout = layout([
    [heading],
    [inputs, p],
])

curdoc().add_root(layout)
