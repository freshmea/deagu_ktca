import matplotlib.pyplot as plt
import numpy as np

count = [0] * 1_000

for i in range(100_000):
    x = np.random.randint(1_000)
    count[x] += 1

x = np.array([i * 50 for i in range(1, 19+1)])
y = np.array(count[50::50])


plt.title("Random number")
plt.xlabel("random")
plt.ylabel("count")

plt.bar(x, y, width=25, color=['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8','C9', 'C10','C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18'])

plt.show()

plt.title("Random number")
plt.xlabel("count")
plt.ylabel("random")
for i in range(len(x)):
    plt.barh(x[i], y[i], height=25)
plt.show()
