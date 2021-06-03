from matplotlib import pyplot as plt
import numpy as np

element = 4
sum_at_n= []
n = []

def t_i(i):
    a = element
    for lp in range(1, i):
        a = 0.5 * a
    return a

def s_N(N):
    s = 0
    for i in range(N):
        s = s + t_i(i+1)
    return s

n_all = list(range(1, 20))
for n in n_all:
    s = s_N(n)
    print (f'The sum of {n} terms is {s}')
    sum_at_n.append(s)
    

plt.plot(n_all, sum_at_n)
plt.xlabel('n')
plt.ylabel('Sn')
plt.show()
