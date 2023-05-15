import matplotlib.pyplot as plt
import numpy as np

plt.title("Trigonometric functions")
plt.xlabel("angle")
plt.ylabel("value")
plt.grid(True, color='darkcyan', alpha=0.5, linestyle='-.')
plt.xlim(-10, 360+10)
plt.ylim(-1.2, 1.2)

x = np.arange(0, 360+1, 10)

sin_y = np.sin(x * np.pi / 180)
cos_y = np.cos(x * np.pi / 180)
plt.plot(x, sin_y, label='sin', color='#f00000', linestyle='-.', marker='o')
plt.plot(x, cos_y, label='cos')

plt.legend(loc=(0.1, 0.1))

plt.xticks([0, 90, 180, 270], ['0d', '90d', '180d', '270d'])
plt.tick_params('y', direction='inout', width=5)

plt.show()
