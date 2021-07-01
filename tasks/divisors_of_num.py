def count_divisors(num):
    count = 0
    i = 1
    for i in range(num):
        if (num % (i + 1)) == 0:
            count += 1
    return count
num = int(input("A number"))
print(num, "has", count_divisors(num), "divisors")
