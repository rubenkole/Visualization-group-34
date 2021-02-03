from bokeh.models import Select
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.models.widgets import Div
from bokeh.layouts import layout
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import pandas as pd
from os.path import dirname, join


# All the options allowed in the drop down menu
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

dataset = pd.read_excel("dataset/improved.xlsx")

positive_dataset = dataset[dataset['SARS-Cov-2 exam result'] == 'positive']
negative_dataset = dataset[dataset['SARS-Cov-2 exam result'] == 'negative']

positive_source = ColumnDataSource(
    data=dict(x=[], y=[], hematocrit=[], age_quantile=[]))
negative_source = ColumnDataSource(
    data=dict(x=[], y=[], hematocrit=[], age_quantile=[]))

# Create figure

# Tool tips occur when the user hovers over the datapoint
TOOLTIPS = [
    ("Hematocrit", "@hematocrit"),
    ("Age quantile", "@age_quantile")
]

p = figure(plot_height=600, plot_width=700, title="", tooltips=TOOLTIPS, toolbar_location="right",
           sizing_mode="scale_both")
p.circle(x="x", y="y", source=positive_source, color="blue", legend="positive", size=6)
p.circle(x="x", y="y", source=negative_source, color="orange", legend="negative", size=6)

p.legend.click_policy = 'hide'


def update():
    # Update the labels on the axes
    p.xaxis.axis_label = x_axis.value
    p.yaxis.axis_label = y_axis.value

    # Update the title
    p.title.text = x_axis.value + " & " + y_axis.value

    # Update the positive source dictionary to contain the current variable
    positive_source.data = dict(
        x=positive_dataset[x_axis.value],
        y=positive_dataset[y_axis.value],
        hematocrit=positive_dataset["Hematocrit"],
        age_quantile=positive_dataset["Patient age quantile"]
    )

    # Update the negative source dictionary to contain the current variable
    negative_source.data = dict(
        x=negative_dataset[x_axis.value],
        y=negative_dataset[y_axis.value],
        hematocrit=negative_dataset["Hematocrit"],
        age_quantile=negative_dataset["Patient age quantile"]
    )


x_axis = Select(title="X-axis", options=sorted(options), value="Serum Glucose")
y_axis = Select(title="Y-axis", options=sorted(options), value="Hemoglobin")

controls = [x_axis, y_axis]

for slider in controls:
    slider.on_change('value', lambda attr, old, new: update())

heading = Div(text=open(join(dirname(__file__), "heading.html")).read(), sizing_mode="stretch_width")

update()

inputs = column(*controls, width=320, height=1000)
inputs.sizing_mode = "fixed"

layout = layout([
    [heading],
    [inputs, p],
])

curdoc().add_root(layout)
