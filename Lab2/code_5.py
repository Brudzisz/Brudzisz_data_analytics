from msilib.schema import File
from cmdstanpy import CmdStanModel
import matplotlib.pyplot as plt

F = len("Maciej")

model1 = CmdStanModel(stan_file="code_7.stan")
model2 = CmdStanModel(stan_file="code_8.stan")
model3 = CmdStanModel(stan_file="code_9.stan")

fit1 = model1.sample(data={"N": F})
fit2 = model2.sample(data={"N": F})
fit3 = model3.sample(data={"N": F})

df1 = fit1.draws_pd()
df2 = fit2.draws_pd()
df3 = fit3.draws_pd()

bins = 30
alpha = 0.5

df1["theta"].hist(bins=bins, alpha=alpha)
df2["theta"].hist(bins=bins, alpha=alpha)
df3["theta"].hist(bins=bins, alpha=alpha)
plt.legend(["Stan_7", "Stan_8", "Stan_9"])
# plt.show()


fit1.save_csvfiles("samples")
fit2.save_csvfiles("samples")
fit3.save_csvfiles("samples")