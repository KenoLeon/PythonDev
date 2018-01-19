#Import Libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read DataFrame ( and parse axis dates)
df = pd.read_csv("visualization/coindeskBTC.csv", usecols=['Date','BTC Close'], parse_dates=['Date'])
df.set_index('Date',inplace=True)
# Seaborn Style:
sns.set(style="darkgrid")
# Same as with matplotlib:
plt.plot(df['BTC Close'])
plt.show()
