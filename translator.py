phrase = input("enter a phrase: ")
new = ""
for letter in phrase:
    if letter in "AEIOUaeiou":
        new = new + "g"
    else:
        new = new + letter
print(new)
#for both lower and uppercase

for letter in phrase:
    if letter in "AEIOUaeiou":
        if letter.isupper():
            new = new + "G"
        else:
            new = new + "g"
    else:
        new = new + letter
print(new)