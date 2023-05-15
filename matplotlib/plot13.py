import matplotlib.pyplot as plt
import numpy as np

plt.title("pie graph")
# plt.xlabel("angle")
# plt.ylabel("value")
# plt.grid(True, color='darkcyan', alpha=0.2, linestyle='-.')

x = np.array([3, 4, 3])
plt.pie(x)
plt.show()