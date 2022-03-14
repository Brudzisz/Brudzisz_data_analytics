from cmdstanpy import CmdStanModel
import pandas as pd
import arviz as az
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

F = len("Maciej")
L = len("Brudzisz")

data = {
    "M": F
}

model = CmdStanModel(stan_file="code_1.stan")

fit = model.sample(data=data)

#Outputs sample draws as pandas dataframe
df = fit.draws_pd()

print(df)

Lambda = df['lambda']

Lambda.plot.hist(bins=30)
plt.suptitle("Lambda")

#Drop removes rows or columns (depending od the second argument)
y_sims = df.drop(df.columns[:3], 1)
y_sims.plot.hist(subplots=True, bins=30)
plt.suptitle("y_sims")

plt.show()