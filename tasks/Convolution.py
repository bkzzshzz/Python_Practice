x = [-1, 2 , 3, 2, 10, 11, 7, 4, -1, -3, -6, -2]
h = [ -100, 100, -1000] 
y = [0, 0]
a= [0,0]
z = []
y.extend(x)
y.extend(a)
print(y)
c = 0
for i in range(len(y) - 2):
    z.append(y[i:i+3])

print(z)
convul = []
sum = 0

for i in range(len(z)):
    for j in range(3):
        sum = sum + z[i][j] * h[j]
    convul.append(sum)

print(convul)
