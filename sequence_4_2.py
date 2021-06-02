from matplotlib import pyplot as plt
import numpy as np

seq = []
element = 4
sum_at_n= []
each_sum = 0
n = []

for i in range(100):
    seq.append(element)
    element = element / 2

for i in  range(100):
    each_sum = 0
    n.append(i)

    for j in range(i+1):
        each_sum = each_sum + seq[j]
       
    sum_at_n.append(each_sum)

print(n)
plt.plot(n, sum_at_n)
plt.xlabel('n')
plt.ylabel('Sn')
plt.show()
    