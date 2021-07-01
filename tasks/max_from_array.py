num = [99, 7, 4, 55, 10, 13, 22]
max = num[1]
for i in range(len(num)):
    if num[i] > max:
        max = num[i]
print(max)