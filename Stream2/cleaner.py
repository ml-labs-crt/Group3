import pandas as pd

f = pd.read_csv("all.csv")
keep_col = ['date','text','geo']
new_f = f[keep_col]
new_f.to_csv("allClean.csv", index=False)