def sum(a):
    c = 0
    for i in range(len(a)):
        c = c + a[i]
    return c

a = [25, 27, 31, 32, 35]
b = []

for i in range(len(a)):
    b.append(a[i]**2)
print(b)
print(f'SD = {(sum(b) / len(a) - (sum(a) / len(a))**2)**0.5}')
