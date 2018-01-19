import pandas as pd
from bokeh.plotting import figure, output_file, show

df = pd.read_csv("visualization/coindeskBTC.csv", usecols=['Date','BTC Close'], parse_dates=['Date'])

output_file("BTC_Price_Chart.html")

# create a new plot with a datetime axis type
p = figure(plot_width=1200, plot_height=800, x_axis_type="datetime")
p.xgrid.grid_line_color = "purple"
p.xgrid.grid_line_alpha = 0.4

p.ygrid.grid_line_color = "purple"
p.ygrid.grid_line_alpha = 0.6
p.ygrid.grid_line_dash = [6, 4]

p.background_fill_color = "Darkgrey"
p.background_fill_alpha = 0.2
p.line(df['Date'], df['BTC Close'], color='cornflowerblue', line_width= 3, alpha=1)

show(p)
