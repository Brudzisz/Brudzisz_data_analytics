from cmd import Cmd
from cmdstanpy import CmdStanModel
import matplotlib.pyplot as plt

N = 0
y = []

with open("normal.csv") as file:
    for line in file:
        value = line.split(",")[1]
        if(value != "value\n"):
            y.append(float(value))
            N += 1

# N = 10
# y = [0, 1, 0, 3, 2, -1, -2, -4, 2, 1]

# N = 5
# y = [1,2,3,0,1]

# N = 1
# y = [1]

data = {
    "N": N,
    "y": y
}

model = CmdStanModel(stan_file="stan1.stan")

fit = model.sample(data=data)

df = fit.draws_pd()
print(df)

bins = 70

plt.subplot(2,1,1)
df["mu"].hist(bins=bins)
plt.title("mu")

plt.subplot(2,1,2)
df["sigma"].hist(bins=bins)
plt.title("sigma")
plt.show()

# Conclusions:
# The more observations there are, the more symmetric the
# probabilistic distribution