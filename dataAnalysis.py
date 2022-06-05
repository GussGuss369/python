import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(1, 2.0 * np.pi,101)
y = np.sin(x)
z = np.sinh(x)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

curve1 = ax1.plot(x, y, label = "sin", color = "r")
curve2 = ax2.plot(x, z, label = "sinh", color = "b")
curves = [curve1, curve2]

ax1.legend()
ax2.legend()
plt.title("Graphs for maths")

plt.show()