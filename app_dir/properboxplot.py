from bokeh.models import Select, FactorRange
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.models.widgets import Div
from bokeh.layouts import layout
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import pandas as pd
from os.path import dirname, join

# All the options allowed in the drop down menu (deemed quantitative)
options = ['Hematocrit', 'Hemoglobin', 'Platelets', 'Mean platelet volume ', 'Red blood Cells', 'Lymphocytes',
           'Mean corpuscular hemoglobin concentration\xa0(MCHC)', 'Leukocytes', 'Basophils',
           'Mean corpuscular hemoglobin (MCH)', 'Eosinophils', 'Mean corpuscular volume (MCV)', 'Monocytes',
           'Red blood cell distribution width (RDW)', 'Serum Glucose', 'Neutrophils', 'Urea',
           'Proteina C reativa mg/dL', 'Creatinine', 'Potassium', 'Sodium', 'Alanine transaminase',
           'Aspartate transaminase', 'Gamma-glutamyltransferase\xa0', 'Total Bilirubin', 'Direct Bilirubin',
           'Indirect Bilirubin', 'Alkaline phosphatase', 'Ionized calcium\xa0', 'Magnesium',
           'pCO2 (venous blood gas analysis)', 'Hb saturation (venous blood gas analysis)',
           'Base excess (venous blood gas analysis)', 'pO2 (venous blood gas analysis)',
           'Total CO2 (venous blood gas analysis)', 'pH (venous blood gas analysis)',
           'HCO3 (venous blood gas analysis)', 'Rods #', 'Segmented', 'Promyelocytes',
           'Metamyelocytes', 'Myelocytes', 'Myeloblasts', 'Urine - Density', 'Urine - Red blood cells',
           'Relationship (Patient/Normal)', 'International normalized ratio (INR)', 'Lactic Dehydrogenase',
           'Creatine phosphokinase\xa0(CPK)\xa0', 'Ferritin', 'Arterial Lactic Acid', 'Lipase dosage', 'Albumin',
           'Hb saturation (arterial blood gases)', 'pCO2 (arterial blood gas analysis)',
           'Base excess (arterial blood gas analysis)', 'pH (arterial blood gas analysis)',
           'Total CO2 (arterial blood gas analysis)', 'HCO3 (arterial blood gas analysis)',
           'pO2 (arterial blood gas analysis)', 'Arteiral Fio2', 'Phosphor', 'ctO2 (arterial blood gas analysis)']

df = pd.read_excel("dataset/improved.xlsx")



# Create the ColumnDataSource for the plot
source = ColumnDataSource(data=dict(cat=[], mean=[], q1=[], q3=[], upper=[], lower=[]))

p = figure(title='Title', x_range=source.data['cat'])

p.vbar('cat', 0.7, 'mean', 'q3', source = source, fill_color="#E08E79", line_color="black")
p.vbar('cat', 0.7, 'q1', 'mean', source = source, fill_color="#3B8686", line_color="black")

p.segment('cat', 'upper', 'cat', 'q3', source = source, color="black")
p.segment('cat', 'lower', 'cat', 'q1', source = source, color="black")



# whiskers (almost-0 height rects simpler than segments)
p.rect('cat', 'lower', 0.2, 0.01, source = source, color="black")
p.rect('cat', 'upper', 0.2, 0.01, source= source, color="black")

p.xgrid.grid_line_color = None

def update():
    af = pd.DataFrame(dict(score=df[y_axis.value], group=df['SARS-Cov-2 exam result']))

    groups = af.groupby('group')

    q1 = groups.quantile(q=0.25)
    mean = groups.quantile(q=0.5)
    q3 = groups.quantile(q=0.75)
    iqr = q3 - q1
    upper = q3 + 1.5 * iqr
    lower = q1 - 1.5 * iqr

    source.data = dict(
        cat=,
        mean=mean,
        q1=q1,
        q3=q3,
        upper=upper,
        lower=lower
    )


    p.title.text = "COVID-19 & " + y_axis.value



y_axis = Select(title="Please select a feature: ", options=sorted(options), value="Hemoglobin")

# When one of the select menus is changed. Run update()
controls = [y_axis]

for control in controls:
    y_axis.on_change('value', lambda attr, old, new: update())

# The heading is a html file can be found under app_dir/heading.html
heading = Div(text=open(join(dirname(__file__), "heading.html")).read(), sizing_mode="stretch_width")

# Update function is called to initialize the variables
update()

# The input column is made so it can fit on the side of the page
inputs = column(*controls, width=320, height=1000)
inputs.sizing_mode = "fixed"

# Layout for the webpage
layout = layout([
    [heading],
    [inputs, p],
])

curdoc().add_root(layout)
