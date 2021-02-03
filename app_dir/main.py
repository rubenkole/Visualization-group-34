from bokeh.models import Select, FactorRange
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.models.widgets import Div
from bokeh.layouts import layout
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import pandas as pd
from os.path import dirname, join

# All the options allowed in the drop down menu (deemed categorical)
options = ['Patient age quantile', 'SARS-Cov-2 exam result', 'Ward', 'Patient addmited to regular ward (1=yes, 0=no)',
           'Patient addmited to semi-intensive unit (1=yes, 0=no)',
           'Patient addmited to intensive care unit (1=yes, 0=no)', 'Respiratory Syncytial Virus', 'Influenza A',
           'Influenza B', 'Parainfluenza 1', 'CoronavirusNL63', 'Rhinovirus/Enterovirus', 'Coronavirus HKU1',
           'Parainfluenza 3', 'Chlamydophila pneumoniae', 'Adenovirus', 'Parainfluenza 4', 'Coronavirus229E',
           'CoronavirusOC43', 'Inf A H1N1 2009', 'Bordetella pertussis', 'Metapneumovirus', 'Parainfluenza 2',
           'Influenza B, rapid test', 'Influenza A, rapid test', 'Strepto A', 'Urine - Esterase', 'Urine - Aspect',
           'Urine - Hemoglobin', 'Urine - Bile pigments', 'Urine - Ketone Bodies', 'Urine - Urobilinogen',
           'Urine - Protein', 'Urine - Leukocytes', 'Urine - Crystals', 'Urine - Hyaline cylinders',
           'Urine - Granular cylinders', 'Urine - Yeasts', 'Urine - Color']

# Load in the improved dataset
df = pd.read_excel("dataset/improved.xlsx")


# Counts the instances of a certain option and returns both the instances and the categories
def counter(option):
    """Counts the instances of a certain option and returns both the instances and the categories"""
    # Count the values of the option and convert it to a dictionary
    my_dict = df[str(option)].value_counts().to_dict()

    # Get the keys from my_dict put them in a list and convert them to a string
    k = list(my_dict.keys())
    key = [str(element) for element in k]

    # Get the values from my_dict put them in a list
    value = list(my_dict.values())

    return key, value


# Create the ColumnDataSource for the plot
source = ColumnDataSource(data=dict(x=[], y=[]))

# Create the figure

# Create the body of the figure. The range depends on the categories
p = figure(title='', x_range=FactorRange(factors=list(source.data['x'])))

# Create the bars
p.vbar(x="x", top="y", width=0.7, source=source)

# Label the x- and y-axis
p.xaxis.axis_label = "Categories"
p.yaxis.axis_label = "Patients"


# Update function gets called when the select menu is changed
def update():
    """Update function gets called everytime the select menu changes"""

    # Update the categories and the amount using the counter() function
    categories, amount = counter(x_axis.value)

    # Update the source dictionary to contain the current variable
    source.data = dict(
        x=categories,
        y=amount
    )

    # Update the x range
    p.x_range.factors = list(source.data['x'])

    # Update the title
    p.title.text = x_axis.value


# Create a select menu to select what feature is to be displayed on the x-axis
x_axis = Select(title="Please select a feature: ", options=sorted(options), value="Influenza A")

# When one of the select menus is changed. Run update()
controls = [x_axis]

for control in controls:
    x_axis.on_change('value', lambda attr, old, new: update())

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
