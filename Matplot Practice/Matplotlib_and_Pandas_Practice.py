import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(1, 2)

df = pd.read_csv(f"C:/Users/Bobno/PycharmProjects/Trading-Bot-Practice/Pandas Practice/market_data.csv")

dates = df["Date"]
highs = df["High"]

axes[0].barh(dates, highs)
axes[1].plot(list(range(15)), highs)

plt.tight_layout()

plt.show()