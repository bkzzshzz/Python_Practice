def exponent(a, b):
    exp = 1
    for i in range(b):
        exp = exp * a
    return exp
print(exponent(9, 2))  