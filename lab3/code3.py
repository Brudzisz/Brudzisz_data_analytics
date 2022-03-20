from cmdstanpy import CmdStanModel
import matplotlib.pyplot as plt

# N = 0
# y = []

# with open("normal.csv") as file:
#     for line in file:
#         value = line.split(",")[1]
#         if(value != "value\n"):
#             y.append(float(value))
#             N += 1

# N = 10
# y = [1,2,3,4,5,6,7,8,9,10]

# N = 2
# y = [10, 10]

N = 4
y = [3, 10, 2, 40]

data1 = {
    "N": N,
    "y": y
}

data2 = {
    "N": N
}

model1 = CmdStanModel(stan_file="stan3.stan")
model2 = CmdStanModel(stan_file="stan4.stan")

fit1 = model1.sample(data=data1)
fit2 = model2.sample(data=data2)

df1 = fit1.draws_pd()
df2 = fit2.draws_pd()

print(df1)
print(df2)

results1 = df1.drop(df1.columns[:9], 1)
results2 = df2.drop(df2.columns[:4], 1)

bins = 50
plt.figure(1)
df1['sigma'].hist(bins = bins)
plt.title("Experimental data")

results1.hist(bins = bins)
plt.title("Experimental data")

plt.figure(3)
df2['sigma'].hist(bins=bins)
plt.title("No experimental data")

results2.hist(bins = bins)
plt.title("No experimental data")
plt.show()

# Conclusion:
# Experimental data shifts the probability distribution plot
# towards the probability distribution of the experimental data