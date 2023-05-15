import matplotlib.pyplot as plt
import numpy as np

def make_sincos(a, b):
    sx = np.arange(a, b, 30)
    cx = sx + 15
    sin_y = np.sin(np.radians(sx))
    cos_y = np.cos(np.radians(cx))
    return sx, cx, sin_y, cos_y

def init_plot():
    plt.title("Trigonometric functions")
    plt.xlabel("value")
    plt.ylabel("angle")
    plt.grid(True, axis='x', color='darkcyan', alpha=0.5, linestyle='-.')

def sincos_plot(a, b):
    sx, cx, sin_y, cos_y = make_sincos(a, b)
    plt.barh(sx, sin_y, label='sin', height=15)
    plt.barh(cx, cos_y, label='cos', height=15)
    plt.legend(loc=(0.7, 0.83))
    plt.yticks([0, 90, 180, 270], ['0d', '90d', '180d', '270d'])

def show_plot():
    plt.show()

def main():
    init_plot()
    sincos_plot(0, 360)
    show_plot()

if __name__ == '__main__':
    main()
