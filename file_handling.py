#file handling: r means read, w means write, r+ means read and write and a means append
#opening file in read mode
country_capital = open("file.txt", "r")
print(country_capital.readable()) #check the file is readable
print("\n")
print(country_capital.read())
print("\n")
print(country_capital.readline()) #prints each line
print(country_capital.readline())

for nation in country_capital.readlines():
    print(nation)

#comment
country_capital.close() #remember to close the file

