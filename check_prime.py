def check_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
        return True
            
            

#num = int(input("A number: "))
print(check_prime(15))
'''if check_prime(num):
    print("Prime")
else:
    print("Not Prime")'''
        