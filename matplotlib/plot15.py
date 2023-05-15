import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.1, 6.0, 1000)
y1 = np.sin(x) ; y2 = np.exp(x) ; y3 = np.log(x) ; y4 = x*x
plt.subplot(221)
plt.plot(x, y1)
plt.subplot(222)
plt.plot(x, y2)
plt.subplot(223)
plt.plot(x, y3)
plt.subplot(224)
plt.plot(x, y4)
plt.show()
