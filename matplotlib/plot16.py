import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.1, 6.0, 1000)

y1 = np.sin(x) ; y2 = np.exp(x) ; y3 = np.log(x)

fig, ((ax1, ax2), (ax3, _)) = plt.subplots(2, 2)

ax1.plot(x, y1)
ax2.plot(x, y2)
ax3.plot(x, y3)
plt.show()
