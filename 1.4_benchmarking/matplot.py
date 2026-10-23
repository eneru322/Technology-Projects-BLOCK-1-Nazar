import matplotlib.pyplot as plt

# Load the numbers (one per line)
with open("results/temperature.txt") as f:
    temps = [float(line.strip()) for line in f]

plt.plot(temps, marker='o')
plt.title("Temperature Over Time")
plt.xlabel("Measurement Number")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
plt.savefig("results/temperature_plot.png")
