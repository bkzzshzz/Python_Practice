def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

list_numbers = [2, 5, 7, 9]
primes  = []

for number in list_numbers:
    if check_prime(number):
        primes.append(number)

print(f'The list of primes is:{primes}')