from matplotlib import pyplot as plt
import math
import numpy as np

def t_i(i, x):
    # i = 1 --> t_i = 2sin(x)
    # i = 2 --> t_i = -1 sin(2x)
    # i = 3 --> t_i = 0.666 sin(3x)
    # i = 4 --> t_i = - 0.5 sin(4x) 
    ti = (2/i)*(-1)**(i+1) * math.sin(i*x)


    # ti = (((-1)**i)/i**2) * math.cos(i*x)
    return ti

def s_N(N, x):
    sum_N = 0
    for i in range(N):
        sum_N += t_i(i+1, x)
    # return math.pi**2/3 + sum_N
    return sum_N


x_all = list(np.arange(-math.pi, math.pi, 0.01))
x_all_all = []
y_all_all = []
for i in range(1, 20):
    y_all = []
    s_all = []
    for x in x_all:
        y_all.append(t_i(i,x))
        s_all.append(s_N(i,x))
    x_all_all.extend(x_all.copy())
    y_all_all.extend(y_all.copy())
    # import matplotlib.pyplot as plt
    plt.plot(x_all_all, y_all_all)
    plt.xlabel('x')
    plt.ylabel(f't_{i}')
    plt.show()

    plt.plot(x_all, s_all)
    plt.xlabel('x')
    plt.ylabel(f'Sum of {i} fucntions')
    plt.show()

        

# y = x