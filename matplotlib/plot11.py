import matplotlib.pyplot as plt
import numpy as np

class NormalPlt:
    def __init__(self, off_set: int, num, repeat, step):
        self.off_set = [i*100/off_set for i in range(off_set)]
        self.num = num
        self.repeat = repeat
        self.step = step

    def init_plot(self):
        plt.title("Random number")
        plt.xlabel("random")
        plt.ylabel("count")

    def make_rand(self):
        self.count = [0] * self.num
        for _ in range(self.repeat):
            self.count[np.random.randint(self.num)] += 1

    def rand_plot(self):
        for value in self.off_set:
            self.make_rand()
            x = np.array([i for i in range(self.step, self.num, self.step)])
            y = np.array(self.count[self.step::self.step])
            plt.bar(x+value, y, width=self.num/self.step/len(self.off_set)*9)

def main():
    norp = NormalPlt(6, 1_000, 10_000, 100)
    norp.init_plot()
    norp.rand_plot()
    plt.show()

if __name__ == '__main__':
    main()
