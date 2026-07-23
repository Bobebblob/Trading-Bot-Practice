import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 1, 2, 0, 3, 5, 2, 1, 0, 1]) # trades taken
y1 = np.array([0, 300, 400, -50, 0, 20, 200, 700, -550, 0, 75]) #daily profit

x2 = np.array([0, 1, 1, 2, 0, 3, 5, 2, 1, 0, 1]) # trades taken
y2 = np.array([0, 210, -300, 75, 0, 150, 200, 320, -120, 0, 120]) #daily profit


plt.scatter(x1, y1, color="black",
            alpha=.75,
            s=50,
            label="January")
plt.scatter(x2, y2, color="red",
            alpha=.75,
            s=50,
            label="February")

plt.legend()

plt.xlabel("Trades Taken")
plt.ylabel("Daily Profit")

plt.show()