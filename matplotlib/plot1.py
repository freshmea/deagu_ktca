import matplotlib.pyplot as plt
import numpy as np

x = np.random.standard_normal(20000)
plt.title("Normal Distribution")
plt.xlabel("value")
plt.ylabel("P")
plt.hist(x, 100)
plt.show()
