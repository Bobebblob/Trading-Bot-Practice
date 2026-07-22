import pandas as pd
from numpy.ma.extras import average

data = {"Date": ["7/1/26", "7/2/26", "7/3/26"],
          "DailyLow": [101.0, 103.0, 105.0],
          "DailyHigh": [102.0, 104.0, 106.0]
        }
df = pd.DataFrame(data, index=["Day1", "Day2", "Day3"])

df["DailyAverage"] = [(df.loc["Day1"]["DailyHigh"] + df.loc["Day1"]["DailyLow"])/2,
                      (df.loc["Day2"]["DailyHigh"] + df.loc["Day2"]["DailyLow"])/2,
                      (df.loc["Day3"]["DailyHigh"] + df.loc["Day3"]["DailyLow"])/2]

new_rows = pd.DataFrame([{"Date": "7/4/26", "DailyLow": 107.0, "DailyHigh": 108.0, "DailyAverage": 107.5},
                         {"Date": "7/5/26", "DailyLow": 109.0, "DailyHigh": 110.0, "DailyAverage": 109.5}], index=["Day4", "Day5"])
df = pd.concat([df, new_rows])

print(df)
#print(df.loc["Day1"])
#print(df.iloc[0])