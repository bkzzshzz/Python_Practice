def fibo(n):
    a = 1
    b = 0
    c = 1

    for i in range(n):
        c = a + b
        a = b
        b = c
        # print(f'{a}, {b}, {c}')
        yield c
    
    # print(f'{a} , {b}, {c}')

print(list(fibo(10)))
