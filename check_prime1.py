def check_prime(num):
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True

print (check_prime(19))