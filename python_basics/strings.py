print("Hotel \\Transylvania")
phrase = "Hotel Transylvania"
#to convert to lower case
print(phrase.lower())
#to convert to upper case
print(phrase.upper())
#check if upper case after convertint to ucase which gives true as it is true
print(phrase.upper().isupper())
#converts to lcase
print(phrase.islower())
#same converts to lower and checks for lcase which gives true
print(phrase.lower().islower())
#Just prints the variable
print(phrase)
#print the number of character is a string
print(len(phrase))
#print the nth letter
#indexing in python starts from 0
print(phrase[8])
#to print from where certain character/s starts 
print(phrase.index("ans"))
#replase characer with other character
print(phrase.replace("Transylvania", "California"))