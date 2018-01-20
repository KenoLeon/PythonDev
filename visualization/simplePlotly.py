# Import Libraries
import plotly as py
import plotly.graph_objs as go
import pandas as pd


# Read DataFrame
df = pd.read_csv("visualization/coindeskBTC.csv", usecols=['Date','BTC Close'], parse_dates=['Date'])

# Basic plotly plot
data = [go.Scatter(
          x=df.Date,
          y=df['BTC Close'])]

py.offline.plot(data)
