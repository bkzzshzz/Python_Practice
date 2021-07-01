from check_prime1 import check_prime
num = int(input("A number: "))
primes = []
for i in range(2, num):
    if check_prime(i):
        primes.append(i)
prime_mul = []
temp_num = num
rem = 0
print(primes)
for i in range(len(primes)):
    rem = 0
    while rem == 0:
        rem = temp_num % primes[i]
        if rem == 0:
            prime_mul.append(primes[i])
            temp_num = temp_num / primes[i]
print(prime_mul)
prompt = ""
for i in range(len(prime_mul)):

    prompt = prompt + str(prime_mul[i]) + "X"
prompt = prompt[:-1]
if check_prime(num):
    print(f'1 X {num} = {num}')
else:
    print(prompt + " = " + str(num))





