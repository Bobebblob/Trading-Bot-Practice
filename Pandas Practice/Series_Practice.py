import pandas as pd

daily_points = [102.2, 103.8, 104.6, 106.5, 101.2]

series = pd.Series(daily_points, index=['day1', 'day2', 'day3', 'day4', 'day5'])

#print(series[series >= 104.0])
#print(series.loc['day1'])
#print(series.iloc[1])

monthly_high = {"january": 101.4, "february": 103.4, "march": 106.8, "april": 107.2}

series2 = pd.Series(monthly_high)

#print(series2)
#print(series2.loc["february"])
#series2.loc["february"] += 1.1
#print(series2.iloc[1])
print(series2[series2 > 101.5])
