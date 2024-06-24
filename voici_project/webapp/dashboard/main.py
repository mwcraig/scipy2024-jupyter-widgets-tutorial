# AUTOGENERATED! DO NOT EDIT! File to edit: ../02c_layout.ipynb.

# %% auto 0
__all__ = ['selected_data_accordion', 'INTRO_TEXT', 'SOURCES_TEXT', 'intro_text', 'data_source_text', 'curve_parameters_layout',
           'curve_parameter_widgets', 'desc_and_ctrl_box', 'data_box', 'main_widget']

# %% ../02c_layout.ipynb 5
# %answer key/dashboard/main.py 6

import ipywidgets as widgets
from .widgets import (year_range, window_size, poly_order, selected_data_grid,
                               update_selected_datagrid, plot_view, output_plot) # import year_range, window_size, poly_order, selected_data_grid, update_selected_datagrid, plot_view, output_plot

# %% ../02c_layout.ipynb 12
# Make the year_range widget description wider to fit the text
year_range.style.description_width = 'initial'

# %% ../02c_layout.ipynb 16
# Change the width of the year_range widget (makes year range selection easier to see)
year_range.layout.width = '500px'

# %% ../02c_layout.ipynb 18
# Change the width of the poly_order widget
poly_order.layout.width = '140px'

# %% ../02c_layout.ipynb 20
# Change the width *and height* of the selected_data_grid widget
selected_data_grid.layout.width = '350px'
selected_data_grid.layout.height = '200px'

# %% ../02c_layout.ipynb 22
selected_data_accordion = widgets.Accordion(titles=('Selected Data',))
selected_data_accordion

# %% ../02c_layout.ipynb 27
# %answer key/dashboard/main.py 28

selected_data_accordion.children = (selected_data_grid,)

# %% ../02c_layout.ipynb 31
# %answer key/dashboard/main.py 32

selected_data_accordion.selected_index = 0

# %% ../02c_layout.ipynb 34
INTRO_TEXT = '''
<p><b>Curve Smoothing</b>
This tool is for smoothing and selecting global mean surface temperature data for visualization. Start by selecting a date
range, and then select the smoothing parameters you want to use. Then click through to the next step, where you will change properties
of the curve smoothing algorithm you selected and visualize the data.
</p>
'''
SOURCES_TEXT = '''
<p>
<b>About Global Mean Surface Temperature Data</b>
<a href="https://climate.nasa.gov/vital-signs/global-temperature/"
target="_blank">Global Temperature (NASA)</a>,
<a href="https://data.giss.nasa.gov/gistemp/graphs/"
target="_blank">GISS Surface Temperature Analysis (NASA)</a>
</p><p>
This site is based on data downloaded from the following site on 2024-06-17:
<a href="https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.csv"
target="_blank">Global Annual Mean Surface Air Temperature Change (NASA)</a>
'''

# %% ../02c_layout.ipynb 36
intro_text = widgets.HTML(value = INTRO_TEXT, layout = widgets.Layout(max_width = '500px'))
data_source_text = widgets.HTML(value = SOURCES_TEXT, layout = widgets.Layout(max_width = '500px'))

# %% ../02c_layout.ipynb 42
# Define the widget containing the curve smoothing parameters
curve_parameters_layout = widgets.Layout(width = '500px', justify_content = 'space-between')
curve_parameter_widgets = widgets.HBox(children = (window_size, poly_order), 
                                       layout=curve_parameters_layout)

# %% ../02c_layout.ipynb 47
# %answer key/dashboard/main.py 47

# Create a VBox to hold the description and control widgets
desc_and_ctrl_box = widgets.VBox()
# add children intro_text, data_source_text, year_range, curve_parameter_widgets
desc_and_ctrl_box.children = (intro_text, data_source_text, year_range, curve_parameter_widgets)

# %% ../02c_layout.ipynb 52
# %answer key/dashboard/main.py 51

# how might we add padding to each of the widgets
for child in desc_and_ctrl_box.children: # how might we add padding to each of the widgets
    child.layout.margin = '15px 0 15px 0'  # top, right, bottom, left

# %% ../02c_layout.ipynb 54
# %answer key/dashboard/main.py 51

# Add a vertical box holding both table and plot visualizations of selected data
data_box = widgets.VBox(children = (selected_data_accordion, plot_view)) # add the selected_data_accordion and the plot_output to a VBox widget called data_box

# %% ../02c_layout.ipynb 57
main_widget = widgets.HBox(children = (desc_and_ctrl_box, data_box))

# %% ../02c_layout.ipynb 60
data_box.layout.margin = '0 0 0 30px'  # top, right, bottom, left
data_box.layout.align_items = 'flex-end'
selected_data_accordion.layout.width = '88%'
desc_and_ctrl_box.layout.min_width = '500px'
