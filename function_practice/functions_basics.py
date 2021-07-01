#creating a function
def say_hi(): #defining a function
    print("Hello!")
say_hi() #calling a function
print("\n")

#a function that takes parameter
def say_hi(name):
    print("Hello " + name + "!")
name = input("Enter your name ")
say_hi(name)

#a function that takes two parameters

def say_hi(name, age):
    print("Hello " + name + ". You are " + age +" years old")
name = input("Name? ")
age= input("Age? ")
say_hi(name, age)

#use return
def cube(num):
    return num * num * num
print(cube(16))