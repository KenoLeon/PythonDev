
#Import Libraries
import matplotlib.pyplot as plt
import pandas as pd

# Read DataFrame ( and parse axis dates)
df = pd.read_csv("visualization/coindeskBTC.csv", usecols=['Date','BTC Close'], parse_dates=['Date'])
# Use Date as index
df.set_index('Date',inplace=True)
# Plot & show
plt.plot(df['BTC Close'])
plt.show()
