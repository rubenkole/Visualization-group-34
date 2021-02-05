import pandas as pd
import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import column, layout, gridplot
from bokeh.models import Select, ColumnDataSource, LassoSelectTool
from bokeh.models.widgets import Div
from bokeh.plotting import figure
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
           'HCO3 (venous blood gas analysis)', 'Rods #', 'Segmented', 'Urine - Density', 'Urine - Red blood cells',
           'Relationship (Patient/Normal)', 'International normalized ratio (INR)', 'Lactic Dehydrogenase',
           'Creatine phosphokinase\xa0(CPK)\xa0', 'Ferritin', 'Arterial Lactic Acid', 'Lipase dosage',
           'Hb saturation (arterial blood gases)', 'pCO2 (arterial blood gas analysis)',
           'Base excess (arterial blood gas analysis)', 'pH (arterial blood gas analysis)',
           'Total CO2 (arterial blood gas analysis)', 'HCO3 (arterial blood gas analysis)',
           'pO2 (arterial blood gas analysis)', 'Arteiral Fio2', 'Phosphor', 'ctO2 (arterial blood gas analysis)']

# Load in the improved dataset
dataset = pd.read_excel("dataset/improved.xlsx")
df = pd.read_excel('dataset/improved.xlsx')

# Sort the dataset into two datasets: Positive and Negative
positive_dataset = dataset[dataset['SARS-Cov-2 exam result'] == 'positive']
negative_dataset = dataset[dataset['SARS-Cov-2 exam result'] == 'negative']

# Create the ColumnDataSource for Positive and Negative
positive_source = ColumnDataSource(
    data=dict(x=[], y=[], hematocrit=[], age_quantile=[], color_pos=[]))
negative_source = ColumnDataSource(
    data=dict(x=[], y=[], hematocrit=[], age_quantile=[], color_neg=[]))

# Create figure

# Tool tips occur when the user hovers over the datapoint
TOOLTIPS = [
    ("Unit", "@hematocrit"),
    ("Age quantile", "@age_quantile")
]

# Create the body of the figure
scatterplot = figure(plot_height=600, plot_width=700, title="", tooltips=TOOLTIPS, toolbar_location="right",
                     sizing_mode="scale_both")

# Create both the circle groups. One for Positive and one for Negative
scatterplot.circle(x="x", y="y", source=positive_source, color="color_pos", legend="positive", size=6)
scatterplot.circle(x="x", y="y", source=negative_source, color="color_neg", legend="negative", size=6)

# Create a legend that will hide the option when clicked
scatterplot.legend.click_policy = 'hide'


# Update function gets called when one of the select menus is changed
def update():
    """Update function gets called everytime on of the select menus change"""
    # Update the labels on the axes
    scatterplot.xaxis.axis_label = x_axis.value
    scatterplot.yaxis.axis_label = y_axis.value

    if color.value == "Normal vision":
        col_pos = "#e40615"
        col_neg = "#8abc25"
    elif color.value == "Deuteranopia":
        col_pos = "#e40615"
        col_neg = "##0066a1"
    elif color.value == "Protania":
        col_pos = "#e40615"
        col_neg = "##84217c"
    elif color.value == "Tritanopia":
        col_pos = "#e40615"
        col_neg = "##0066a1"

    col_pos_list = []
    for i in range(len(positive_dataset[x_axis.value])):
        col_pos_list.append(col_pos)

    # Update the title
    scatterplot.title.text = x_axis.value + " & " + y_axis.value

    # Update the positive source dictionary to contain the current variable
    positive_source.data = dict(
        x=list(positive_dataset[x_axis.value]),
        y=list(positive_dataset[y_axis.value]),
        hematocrit=list(positive_dataset["Ward"]),
        age_quantile=list(positive_dataset["Patient age quantile"]),
        color_pos=col_pos_list
    )

    col_neg_list = []

    for i in range(len(negative_dataset[x_axis.value])):
        col_neg_list.append(col_neg)

    # Update the negative source dictionary to contain the current variable
    negative_source.data = dict(
        x=list(negative_dataset[x_axis.value]),
        y=list(negative_dataset[y_axis.value]),
        hematocrit=list(negative_dataset["Ward"]),
        age_quantile=list(negative_dataset["Patient age quantile"]),
        color_neg=col_neg_list
    )

    # =======================================================================
    # Code for the boxplot of COVID 19 and the Y-axis
    q1, mean, q3, upper, lower = boxplotcalculators(y_axis.value)

    source.data = dict(
        cat=cats_creator(),
        mean=mean,
        q1=q1,
        q3=q3,
        upper=upper,
        lower=lower
    )

    p.title.text = "COVID-19 & " + y_axis.value

    # =======================================================================

    # Code for the boxplot of COVID 19 and the X-axis
    x_q1, x_mean, x_q3, x_upper, x_lower = boxplotcalculators(x_axis.value)

    x_source.data = dict(
        cat=cats_creator(),
        mean=x_mean,
        q1=x_q1,
        q3=x_q3,
        upper=x_upper,
        lower=x_lower
    )

    px.title.text = "COVID-19 & " + x_axis.value


# =============================================================================
# Code for the boxplot of COVID-19 and the X-axis

def boxplotcalculators(feature):
    """Calculates the quantiles for a boxplot and converts them to a list"""
    af = pd.DataFrame(dict(score=df[str(feature)], group=df['SARS-Cov-2 exam result']))

    groups = af.groupby('group')

    q1 = list(groups.quantile(q=0.25).score)
    mean = list(groups.quantile(q=0.5).score)
    q3 = list(groups.quantile(q=0.75).score)
    iqr = np.asarray(q3) - np.asarray(q1)
    upper = list(q3 + 1.5 * iqr)
    lower = list(q1 - 1.5 * iqr)
    return q1, mean, q3, upper, lower


def cats_creator():
    """Creates the appropriate binary categorical inputs (of the SARS-Cov-2 exam result) for a boxplot in the Bokeh library"""
    data = [{'group': 'negative', 'score': 1},
            {'group': 'positive', 'score': 1}]

    drf = pd.DataFrame(data, index=['negative', 'positive'])
    drf1 = drf.reset_index()
    drf2 = drf1["group"]
    drf2 = list(drf2)

    return drf2


# Create the ColumnDataSource for the plot

source = ColumnDataSource(data=dict(cat=[], mean=[], q1=[], q3=[], upper=[], lower=[]))

q1, mean, q3, upper, lower = boxplotcalculators("Hemoglobin")

source.data = dict(
    cat=cats_creator(),
    mean=mean,
    q1=q1,
    q3=q3,
    upper=upper,
    lower=lower
)

p = figure(title='Title', x_range=source.data['cat'])

p.segment('cat', 'upper', 'cat', 'q3', source=source, color="black")
p.segment('cat', 'lower', 'cat', 'q1', source=source, color="black")

p.vbar('cat', 0.7, 'mean', 'q3', source=source, fill_color="#e40615", line_color="black")
p.vbar('cat', 0.7, 'q1', 'mean', source=source, fill_color="#000000", line_color="black")

# whiskers (almost-0 height rects simpler than segments)
p.rect('cat', 'lower', 0.2, 0.01, source=source, color="black")
p.rect('cat', 'upper', 0.2, 0.01, source=source, color="black")

p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = "white"
p.grid.grid_line_width = 2
p.xaxis.major_label_text_font_size = "16px"

# =============================================================================


x_source = ColumnDataSource(data=dict(cat=[], mean=[], q1=[], q3=[], upper=[], lower=[]))

x_q1, x_mean, x_q3, x_upper, x_lower = boxplotcalculators("Hemoglobin")

x_source.data = dict(
    cat=cats_creator(),
    mean=x_mean,
    q1=x_q1,
    q3=x_q3,
    upper=x_upper,
    lower=x_lower
)

px = figure(title='Title', x_range=x_source.data['cat'])

px.segment('cat', 'upper', 'cat', 'q3', source=x_source, color="black")
px.segment('cat', 'lower', 'cat', 'q1', source=x_source, color="black")

px.vbar('cat', 0.7, 'mean', 'q3', source=x_source, fill_color="#e40615", line_color="black")
px.vbar('cat', 0.7, 'q1', 'mean', source=x_source, fill_color="#000000", line_color="black")

# whiskers (almost-0 height rects simpler than segments)
px.rect('cat', 'lower', 0.2, 0.01, source=x_source, color="black")
px.rect('cat', 'upper', 0.2, 0.01, source=x_source, color="black")

px.xgrid.grid_line_color = None
px.ygrid.grid_line_color = "white"
px.grid.grid_line_width = 2
px.xaxis.major_label_text_font_size = "16px"

# =============================================================================

# Create two select menus. One for the x-axis and one for the y-axis
x_axis = Select(title="X-axis", options=sorted(options), value="Serum Glucose")
y_axis = Select(title="Y-axis", options=sorted(options), value="Hemoglobin")
color = Select(title="Color blindness", options=["Normal vision", "Deuteranopia", "Protania", "Tritanopia"],
               value="Normal vision")

# When one of the select menus is changed. Run update()
controls = [x_axis, y_axis, color]

for slider in controls:
    slider.on_change('value', lambda attr, old, new: update())

# The heading is a html file can be found under app_dir/heading.html
heading = Div(text=open(join(dirname(__file__), "heading.html")).read(), sizing_mode="stretch_width")

# Update function is called to initialize the variables
update()

# The input column is made so it can fit on the side of the page
inputs = column(*controls, width=320, height=1000)
inputs.sizing_mode = "fixed"

grid = gridplot([[scatterplot, p], [px, None]])

# Layout for the webpage
layout = layout([
    [heading],
    [inputs, grid],
])

curdoc().add_root(layout)
