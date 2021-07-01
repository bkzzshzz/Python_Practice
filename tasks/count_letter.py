def count_letter(word, letter):
    count = 0
    for every_letter in word:
        if every_letter == letter:
            count += 1
    return count
word = input("A Word: ")
letter = input("A letter: ")
print(letter + "repeats " + str(count_letter(word,letter)) + " in " + word)
        
