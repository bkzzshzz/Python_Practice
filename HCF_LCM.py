def find_hcf(a , b):
    divisors_a = []
    divisors_b = []
    common_divisors = []
    for i in range(1, a + 1):
        if (a % i) == 0:
            divisors_a.append(i)
    for j in range(1, b + 1):
        if (b % j) == 0:
            divisors_b.append(j)
    for i in range(len(divisors_a)):
        for j in range(len(divisors_b)):
            if divisors_a[i] == divisors_b[j]:
                common_divisors.append(divisors_a[i])
    return common_divisors[-1]

    #print(divisors_a)

a = int(input("A Number: "))
b = int(input("A Number: "))
hcf = find_hcf(a , b)
print(f'The hcf is {hcf}')
lcm = (a * b) / int(hcf)
print(f'LCM is {lcm}')
