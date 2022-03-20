import os
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel

dataset = {
    "N": 14,
    "y": [0,0,0,0,0,0,1,1,1,1,1,1,1,1]
    }
    
stan_file = os.path.join("bern_1.stan")
model = CmdStanModel(stan_file=stan_file)
fit = model.sample(data=dataset)

theta = fit.stan_variable(var='theta')

summary = fit.summary()
theta_summary = summary.loc['theta']
theta_mean = theta_summary[0]
theta_95 = theta_summary[5]
theta_median = theta_summary[4]
theta_5 = theta_summary[3]

#PLOTTING
fig, ax = plt.subplots()
counts, bins, bars = plt.hist(theta, alpha=0.8)
max_count = max(counts)

ax.axvline(theta_median, linestyle=":")
ax.text(theta_median+0.01, max_count, "Median")

ax.axvline(theta_mean, linestyle=":")
ax.text(theta_mean-0.07, max_count, "Mean")

ax.axvline(theta_95, linestyle=":")
ax.text(theta_95+0.01, max_count, "95%")

ax.axvline(theta_5, linestyle=":")
ax.text(theta_5+0.01, max_count, "5%")
plt.show()
