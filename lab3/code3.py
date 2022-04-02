from cmdstanpy import CmdStanModel
import matplotlib.pyplot as plt
import pandas as pd

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

# N = 4
# y = [3, 10, 2, 40]

# data1 = {
#     "N": N,
#     "y": y
# }

# data2 = {
#     "N": N
# }


normal_csv = pd.read_csv('normal.csv', index_col=0, header=0)

data1 = {
    "N": len(normal_csv['value']),
    "y": normal_csv['value'].to_list()
}

data2 = {
    "N": len(normal_csv['value'])
}

model1 = CmdStanModel(stan_file="stan3.stan")
model2 = CmdStanModel(stan_file="stan4.stan")

fit1 = model1.sample(data=data1)
fit2 = model2.sample(data=data2)

df1 = fit1.draws_pd()
df2 = fit2.draws_pd()

print(df1)
print(df2)


bins = 50
plt.subplot(2,1,1)
df1['sigma'].hist(bins = bins)
plt.title("Sigma")
plt.subplot(2,1,2)
df1['y_rep[1]'].hist(bins = bins)
plt.title("y_rep")
plt.suptitle("With experimental data")


plt.figure(2)
plt.subplot(2,1,1)
df2['sigma'].hist(bins=bins)
plt.title("Sigma")
plt.subplot(2,1,2)
df2['y_prior[1]'].hist(bins = bins)
plt.title("y_prior")
plt.suptitle("Without experimental data")
plt.show()

# Conclusion:
# Experimental data shifts the probability distribution plot
# towards the probability distribution of the experimental data