try:
    #value = 10/0
    number = int(input("enter a number: "))
    print(number)

    
except ZeroDivisionError: 
    print("Divided by zero")
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
        print(err)    