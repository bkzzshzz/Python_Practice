#Learning about list
#List is a structure to organize multiple data

cities = ["Kathmandu", "Pokhara", "Butwal", "Biratnagar", "Dipayal"]
print(cities)

#Indexing lists...also begins with 0 
print("\n" + cities[2])

#indexing the back of the list begins with -1 
print("\n" + cities[-1])

#to index within a range
print(cities[1:3]) #prints from index 1 to 2...exludes the fourth
print(cities[2:]) #prints everthing after pos 2

#update a value manually
cities[0] = "Bhaktapur"

print(cities[0])
