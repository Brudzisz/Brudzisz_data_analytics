from cmdstanpy import CmdStanModel
import matplotlib.pyplot as plt
import pandas as pd

coin_csv = pd.read_csv('coin.csv', index_col=0, header=0)

data = {
    "N": len(coin_csv['Toss_Result']),
    "y": coin_csv['Toss_Result'].to_list()
}

model = CmdStanModel(stan_file="stan2.stan")
fit = model.sample(data)
df = fit.draws_pd()

# print(df)
 
bins = 50
df["theta"].hist(bins = bins)
plt.title('Theta')
plt.show()