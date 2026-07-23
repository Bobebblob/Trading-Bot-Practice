from math import log

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])

figure, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, x, color="blue")
axes[0, 1].bar(x, x**0.5, color="red")
axes[1, 0].plot(x, x*-2, color="green")
axes[1, 1].scatter(x, x*x, color="black")

plt.tight_layout()
plt.show()

