
#Import Libraries
from bokeh.models import HoverTool
from bokeh.plotting import figure, show, output_file
import pandas as pd

# Read Data
df = pd.read_csv("correlation/weatherIceCream.csv", usecols=['Date','AVG temp C','Ice Cream production'])

hover = HoverTool(tooltips=[
    ("(Temp,Ice Cream Production", "($x, $y)")
])

p = figure(x_range=(-10, 30),y_range=(35, 90), tools=[hover])

# Main chart definition
p.scatter(df['AVG temp C'], df['Ice Cream production'],size=10)

p.background_fill_color = "mintcream"
p.background_fill_alpha = 0.2
p.xaxis.axis_label = "Avg Temp C"
p.yaxis.axis_label = "Ice Cream Production (1000, Gallons)"

show(p)
