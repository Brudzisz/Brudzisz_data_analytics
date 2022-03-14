from cmdstanpy import CmdStanModel
import matplotlib.pyplot as plt

F = len("Maciej")
L = len("Brudzisz")

model = CmdStanModel(stan_file="code_6.stan")

data = {
    "y_guess": [2],
    "theta": [(F+L)/2]
}

fit = model.sample(data)

df = fit.draws_pd()
print(df)
print("(F+L)/2 = ", str((F+L)/2))