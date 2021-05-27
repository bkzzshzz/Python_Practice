'''#using boolean for if
is_male = False
is_tall = True
if is_male:
    print("You are a man")
else:
    print("You are not a man")

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not(is_tall):
    print("You are a male but not tall")
elif not(is_male) and is_tall:
    print("You are not male but tall")
else:
    print("You are either not male, or tall or both")'''

def max(a, b, c):
    if a > b and a > c:
        print(a, "is the greatest")
    elif b > a and b > c:
        print(b, "is the greatest")
    elif c > a and c > b:
        print(c, "is the greatest")
    else:
        print("They are equal") 
max(2,2,9)

#using return makes code less bulky
def max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        print("They are equal")
        return 
print(max(2,2,2))