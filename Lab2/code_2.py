from cmdstanpy import CmdStanModel
import matplotlib.pyplot as plt

model1 = CmdStanModel(stan_file="code_2.stan")
model2 = CmdStanModel(stan_file="code_3.stan")

# This one raises error (y values greater than 1)
# data = {
#     "N": 5,
#     "y": [0,1,2,3,4,5]
# }

data = {
    "N": 5,
    "y": [0,1,1,0,1]
}

fit1 = model1.sample(data)
fit2 = model2.sample(data)

df1 = fit1.draws_pd()
df2 = fit2.draws_pd()

print(df1)
print(df2)

plt.subplot(2, 1, 1)
df1["theta"].plot.hist()
plt.title("Code 2")
plt.subplot(2,1,2)
df2["theta"].plot.hist()
plt.title("Code 3")
plt.show()
