from cmd import Cmd
from cmdstanpy import CmdStanModel
import matplotlib.pyplot as plt
import pandas as pd

normal_csv = pd.read_csv('normal.csv', index_col=0, header=0)
model = CmdStanModel(stan_file="stan1.stan")

data1 = {
    "N": 1,
    "y": [normal_csv['value'][0]]
}

data2 = {
    "N": len(normal_csv['value']),
    "y": normal_csv['value'].to_list()
}

fit1 = model.sample(data=data1)
fit2 = model.sample(data=data2)

df1 = fit1.draws_pd()
df2 = fit2.draws_pd()
print(df1)
print(df2)

bins = 70
plt.figure(1)
plt.subplot(2,1,1)
df1["mu"].hist(bins=bins)
plt.title("mu")

plt.subplot(2,1,2)
df1["sigma"].hist(bins=bins)
plt.title("sigma")


plt.figure(2)
plt.subplot(2,1,1)
df2["mu"].hist(bins=bins)
plt.title("mu")

plt.subplot(2,1,2)
df2["sigma"].hist(bins=bins)
plt.title("sigma")
plt.show()

# Conclusions:
# The more observations there are, the wider range
# of predictions and higher sigma
