#Import Libraries
import pandas as pd
from bokeh.plotting import figure, output_file, show

# Read DataFrame and parse x axis dates
df = pd.read_csv("visualization/coindeskBTC.csv", usecols=['Date','BTC Close'], parse_dates=['Date'])
# Notice we don't need to set the index, bokeh takes care of that
output_file("BTC_Price_Chart.html")
# create a new plot with a datetime axis type
p = figure(plot_width=1200, plot_height=800, x_axis_type="datetime")
# Add the series with some minimal styling
p.line(df['Date'], df['BTC Close'], color='cornflowerblue', line_width= 3, alpha=1)
show(p)
