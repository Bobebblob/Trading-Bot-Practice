import csv

daily_data = []

with open("Daily_highs_and_lows.csv", "a") as file:
    Date = input("What is the date? Type 's' for skip ")
    if Date != 's':
        writer = csv.DictWriter(file, fieldnames=["date", "low", "high"])
        HoD = input("What is the high of day? ")
        LoD = input("What is the low of day? ")
        writer.writerow({"date": Date, "low": LoD, "high": HoD})

with open("Daily_highs_and_lows.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        day_total = {
            "date": row["date"],
            "low": row["low"],
            "high": row["high"]
        }
        daily_data.append(day_total)

sort_request = input("For sorting by date use 'd', for sorting by low use 'l', and for sorting by high use 'h': ")
if sort_request == 'd':
    sort_param = "date"
elif sort_request == 'l':
    sort_param = "low"
else:
    sort_param = "high"

for day in sorted(daily_data, key=lambda day: day[sort_param]):
    print(f'date: {day["date"]} low: {day["low"]} high: {day["high"]}')