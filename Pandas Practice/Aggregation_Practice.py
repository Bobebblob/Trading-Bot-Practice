import pandas as pd

df = pd.read_csv("market_data.csv")

market_group = df.groupby("Market")

print(market_group["Volume"].min())
print(market_group["Volume"].max())

#print(df["Volume"].mean())
#print(df["Returns"].sum())
#print(df["Open"].min())
#print(df["Close"].max())
#print(df["Date"].count())


#print(df.to_string())
#print(df.mean(numeric_only=True))
#print(df.sum(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.count())