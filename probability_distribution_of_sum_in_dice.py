# alist = [[1,2] , [2,3]]
# blist = [4, 5]
# alist[0][0] = 2
# alist.append(blist)
# print(alist)
# print(alist[0][0])
import random
def sum(a):
    return a[0] + a[1]

possibilities = []
each_possibility = [None] * 2
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
count_8 = 0
count_9 = 0
count_10 = 0
count_11 = 0
count_12 = 0
for i in range(1000):
    
    for j in range(2):
        
        each_possibility[j] =  random.randint(1, 6)
    

    possibilities.append(each_possibility.copy())
each_possibility = []
for i in range(10):
    each_possibility = possibilities[i]
    if sum(each_possibility) == 2:
        count_2 = count_2 + 1
    elif sum(each_possibility) == 3:
        count_3 += 1
    elif sum(each_possibility) == 4:
        count_4 += 1
    elif sum(each_possibility) == 5:
        count_5 += 1
    elif sum(each_possibility) == 6:
        count_6 += 1
    elif sum(each_possibility) == 7:
        count_7 += 1
    elif sum(each_possibility) == 8:
        count_8 += 1
    elif sum(each_possibility) == 9:
        count_9 += 1
    elif sum(each_possibility) == 10:
        count_10 += 1
    elif sum(each_possibility) == 11:
        count_11 += 1
    elif sum(each_possibility) == 12:
        count_12 += 1
print(f'The probabity of sum being 2 is {count_2 / 1000}')
print(f'The probabity of sum being 3 is {count_3 / 1000}')
print(f'The probabity of sum being 4 is {count_4 / 1000}')
print(f'The probabity of sum being 5 is {count_5 / 1000}')
print(f'The probabity of sum being 6 is {count_6 / 1000}')
print(f'The probabity of sum being 7 is {count_7 / 1000}')
print(f'The probabity of sum being 8 is {count_8 / 1000}')
print(f'The probabity of sum being 9 is {count_9 / 1000}')
print(f'The probabity of sum being 10 is {count_10 / 1000}')
print(f'The probabity of sum being 11 is {count_11 / 1000}')
print(f'The probabity of sum being 12 is {count_12 / 1000}')



    

# each_possibility.append(possibilities[2])
# print(each_possibility)
# print(possibilities)

# print(possibilities[1][1])



