import pandas as pd

df = pd.read_csv("corrupt_market_data.csv")

df = df.drop(columns=["SMA_5", "Adj Close"])

#df = df.dropna(subset=["Close", "Open", "Volume"])

#df = df.fillna({"Close": "Unknown", "Volume": "Unknown"})
df = df.fillna({"Ticker": "AAPL"})

df["Market"] = df["Market"].replace({"NASDQ": "NASDAQ"})
df["Market"] = df["Market"].str.upper()

try:
    df["Volume"] = df["Volume"].astype(int)
except ValueError:
    exit

df = df.drop_duplicates()

print(df.to_string())