import matplotlib.pyplot as plt

highs = [101.2, 103.5, 108.4]
lows = [100.2, 102.5, 107.4]
days = ["Monday", "Tuesday", "Wednesday"]

line_style = dict(marker=".",
         markersize="15",
         markerfacecolor="blue",
         linestyle="dashed",
         linewidth=2)

plt.title("Practice Title", fontsize=15,
          family="Arial",
          fontweight="bold",
          color="black")

plt.xlabel("Day of Week", fontsize=10,
           family="Arial",
           color="blue")

plt.ylabel("Points", fontsize=10,
           family="Arial",
           color="blue")

#plt.xticks()
plt.tick_params(axis="both",
                colors="black")

plt.grid(axis="y",
         linewidth=2,
         color="gray",
         linestyle="dashed")

plt.plot(days, highs, color="red", **line_style)
plt.plot(days, lows, color="blue")
plt.show()