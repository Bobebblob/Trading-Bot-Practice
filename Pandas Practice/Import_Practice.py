import pandas as pd

df = pd.read_csv("market_data.csv", index_col="Date")

day = input("Enter the date in the following format YYYY-MM-DD : ")

try:
    print(df.loc[day])
except KeyError:
    print(f"{day} not found")

#print(df)
#print(df.iloc[0:7:2, 0:3])
#print(df.loc["2026-07-07": "2026-07-10", ["Open", "High", "Low"]])
#print(df.iloc[10])
#print(df[["Date", "High", "Low"]])
#print(df["Date"])
#print(df.to_string())