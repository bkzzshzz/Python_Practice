card_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
card_group = ["Spade", "Club", "Heart", "Diamond"]
print(card_group)
#append one list to another using extend; will be added after the last element
card_group.extend(card_number)
print(card_group)

#append external data to a list; goes to last position
card_number.append("A") #append only takes *one* input
print(card_number)

#insert data at a certain position
card_number.insert(0, "A")
print(card_number)

#remove an element
card_number.remove("A")
print(card_number)

#to remove the last element using pop
card_number.pop()
print(card_number)

#Clear all
card_number.clear()
print(card_number)

card_number = [1, 2, 3, 4, 5, 6, 7, 4, 9, 10, 11, 10]
card_number.append("A")


#to check is an element is in the list
print(card_number.index("A"))
print(card_number.index(5))
print(card_number.index(2))

#to count how many times an element repeats
print(card_number.count(10))

#sort(arrange from ascending) a list
card_number.pop()
print(card_number)
card_number.sort()
print(card_number)
card_group = ["Spade", "Club", "Heart", "Diamond"]
card_group.sort()
print(card_group)

#reverse
card_group.reverse()
print(card_group)
card_number.reverse()
print(card_number)

#make a copy of lists using copy
card_group2 = card_group
print(card_group2)
card_group2 = card_group.copy()
print(card_group2)