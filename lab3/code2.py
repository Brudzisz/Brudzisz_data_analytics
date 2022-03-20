from cmdstanpy import CmdStanModel
import matplotlib.pyplot as plt

N = 0
y = []

with open("coin.csv") as file:
    for line in file:
        try:
            outcome = int(line.split(",")[1])
            y.append(outcome)
            N += 1
        except:
            continue

print(y)

# N = 2
# y = [1,1]

data = {
    "N": N,
    "y": y
}

model = CmdStanModel(stan_file="stan2.stan")

fit = model.sample(data)

df = fit.draws_pd()

print(df)
 

bins = 50
df["theta"].hist(bins = bins)
plt.show()