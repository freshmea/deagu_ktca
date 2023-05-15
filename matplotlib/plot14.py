import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.1, 6.0, 1000)
y1 = np.sin(x)
y2 = np.exp(x)
y3 = np.log(x)
plt.plot(x, y1)
plt.show()
plt.plot(x, y2)
plt.show()
plt.plot(x, y3)
plt.show()
