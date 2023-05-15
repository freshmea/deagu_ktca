import matplotlib.pyplot as plt
import numpy as np

def make_rand(n, m):
    count = [0] * n
    for _ in range(m):
        count[np.random.randint(n)] += 1
    return count

def init_plot():
    plt.title("Random number")
    plt.xlabel("random")
    plt.ylabel("count")

def rand_plot(x_offset, n, m, s):
    r = make_rand(n, m)
    x = np.array([i * 100 for i in range(1, 9+1)])
    y = np.array(r[s::s])
    plt.bar(x+x_offset, y, width=5)

def show_plot():
    plt.show()

if __name__ == '__main__':
    init_plot()
    for x_offset in [i*5 for i in range(16)]:
        rand_plot(x_offset, 1_000, 1_000_000, 100)
    show_plot()
