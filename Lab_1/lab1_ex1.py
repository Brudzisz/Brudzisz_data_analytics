import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Data1.csv", index_col="Unnamed: 0")
df.plot()

df.plot.hist(bins=10)

df.plot.kde()

period = (df.index >= "2018-1-1") & (df.index <= "2018-12-31")
new_df = df.loc[period][["theta_1", "theta_2", "theta_3", "theta_4"]]
print(new_df)

new_df.plot()
new_df.plot.hist(bins=10)
new_df.plot.kde()
plt.show()