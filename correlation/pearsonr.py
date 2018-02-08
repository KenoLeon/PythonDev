from scipy.stats import pearsonr

import pandas as pd
# Read Data
df = pd.read_csv("correlation/weatherIceCream.csv", usecols=['Date','AVG temp C','Ice Cream production'])

# pearson in the hauz !
print(pearsonr(df['AVG temp C'],df['Ice Cream production']))
