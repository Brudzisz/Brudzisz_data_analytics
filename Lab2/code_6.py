from cmdstanpy import CmdStanModel
import matplotlib.pyplot as plt
import pandas

F = len("Maciej")
data = {"N": F}

model = CmdStanModel(stan_file="code_10.stan")

previous_samples1 = ["samples/sample1_1.csv", "samples/sample1_2.csv", "samples/sample1_3.csv", "samples/sample1_4.csv"]
previous_samples2 = ["samples/sample2_1.csv", "samples/sample2_2.csv", "samples/sample2_3.csv", "samples/sample2_4.csv"]
previous_samples3 = ["samples/sample3_1.csv", "samples/sample3_2.csv", "samples/sample3_3.csv", "samples/sample3_4.csv"]

fit1 = model.generate_quantities(data=data, mcmc_sample=previous_samples1)
fit2 = model.generate_quantities(data=data, mcmc_sample=previous_samples2)
fit3 = model.generate_quantities(data=data, mcmc_sample=previous_samples3)

df1 = fit1.draws_pd()
df2 = fit2.draws_pd()
df3 = fit3.draws_pd()

bins = 50

plt.subplot(3,1,1)
df1["mean_y"].hist(bins=bins)

plt.subplot(3,1,2)
df2["mean_y"].hist(bins=bins)

plt.subplot(3,1,3)
df3["mean_y"].hist(bins=bins)

plt.suptitle("mean_y")
plt.show()