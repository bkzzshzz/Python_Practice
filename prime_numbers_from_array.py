list_numbers = [2, 5, 7, 9]
primes  = []
for i in range(len(list_numbers)):
    for j in range(2, list_numbers[i]):
            if (list_numbers[i] % j) == 0:
                break
    primes[i] = list_numbers[i]

print(primes)
                
        