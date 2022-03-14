from cmdstanpy import CmdStanModel
import matplotlib.pyplot as plt
from scipy.stats import gamma
import numpy as np

model1 = CmdStanModel(stan_file="code_4.stan")
model2 = CmdStanModel(stan_file="code_5.stan")

fit1 = model1.sample()
fit2 = model2.sample()

df1 = fit1.draws_pd()
df2 = fit2.draws_pd()

print("DF1: ")
print(df1)

print("DF2: ")
print(df2)

#Checking sampler transitions for divergences showed ~34% of transitions with a divergence
print("DIAGNOSE FIT 1:" )
print(fit1.diagnose())

#Checking sampler transitions for divergences showed no transitions with a divergence
print("DIAGNOSE FIT 2:" )
print(fit2.diagnose())


#Probability density function
x = np.linspace(0,7,1000)
#a = alpha; scale = 1/beta
y = gamma.pdf(x, a=1.25, scale=1/1.25)


plt.subplot(2,2,3)
plt.plot(x, y)

plt.subplot(2,2,1)
df1["theta"].hist(bins=50)
plt.xlim = 7
plt.suptitle("Stan_4 code")

plt.subplot(2,2,2)
df2["theta"].hist(bins=50)
plt.xlim = 7

plt.subplot(2,2,4)
plt.plot(x,y)
plt.show()