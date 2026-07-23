import matplotlib.pyplot as plt
import numpy as np

profit = np.random.normal(loc=100, scale=100, size=100) #loc=mean, scale=stdev, size=samplesize

#profit = np.clip(profit, 0, 200)

plt.hist(profit,
         bins=10,
         color="black",
         edgecolor="white")

plt.xlabel("Daily Profit")
plt.ylabel("Num Days")
plt.title("Daily Profit Simulation")
plt.show()