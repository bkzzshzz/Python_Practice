sentence = input("A sentence: ")
new_sentence = ""
for i in sentence:
    if i in "aeiouAEIOU":
        sum = 1
    else:
        new_sentence = new_sentence + i
        
print(new_sentence)