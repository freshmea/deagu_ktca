import matplotlib.pyplot as plt
import numpy as np

class Trigonal:
    def __init__(self, min, max, step = 30):
        self.min = min
        self.max = max
        self.step = step

    def make_sincos(self):
        self.sx = np.arange(self.min, self.max, self.step)
        self.cx = self.sx + self.step/2
        self.sin_y = np.sin(np.radians(self.sx))
        self.cos_y = np.cos(np.radians(self.cx))

    def init_plot(self):
        plt.title("Trigonometric functions")
        plt.xlabel("value")
        plt.ylabel("angle")
        plt.grid(True, axis='x', color='darkcyan', alpha=0.5, linestyle='-.')

    def sincos_plot(self):
        self.make_sincos()
        plt.barh(self.sx, self.sin_y, label='sin', height=self.step/2)
        plt.barh(self.cx, self.cos_y, label='cos', height=self.step/2)
        plt.legend(loc=(0.7, 0.83))
        plt.yticks([0, 90, 180, 270], ['0d', '90d', '180d', '270d'])

def main():
    tri = Trigonal(0, 360, 1)
    tri.init_plot()
    tri.sincos_plot()
    plt.show()

if __name__ == '__main__':
    main()
