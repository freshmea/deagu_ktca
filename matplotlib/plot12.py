import matplotlib.pyplot as plt
import numpy as np

plt.title("Trigonometric functions")
plt.xlabel("angle")
plt.ylabel("value")
plt.grid(True, color='darkcyan', alpha=0.2, linestyle='-.')

x = np.arange(0, 360+1, 10)
sin_y = np.sin(np.radians(x))
area = np.abs(sin_y) * 500
color = area
alpha = 0.5

plt.scatter(x, sin_y, s=area, c=color, alpha=alpha, cmap='hsv')

plt.colorbar()

plt.xticks([0, 90, 180, 270], ['0d', '90d', '180d', '270d'])

plt.show()
