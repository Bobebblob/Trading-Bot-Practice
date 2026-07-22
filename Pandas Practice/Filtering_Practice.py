import pandas as pd

df = pd.read_csv("market_data.csv", index_col="Date")

high_volume = df[(df["Volume"] >= 30000000) & (df["Returns"] > 0)]
bull_days = df[df["Open"] <= df["Low"] + 0.5]
bear_days = df[df["Open"] >= df["Low"] + 0.5]

print(high_volume.to_string())
#print(bull_days)
#print(bear_days)