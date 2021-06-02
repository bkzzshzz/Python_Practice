from matplotlib import pyplot as plt
import numpy as np

def quad(x, a, b ,c):
    y = []

    for i in range(len(x)):
        y.append(a * x[i] ** 3 + b * x[i] + c)
    return y



if __name__ == '__main__':
    x = []
    x = list(np.arange(-10, 10, 0.1))
    y = quad(x, 1, 2, 3)
    print(len(x), len(y))
    plt.plot(x, y)
    plt.show()
