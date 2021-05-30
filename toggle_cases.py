def toggle(character):
    if character.isupper():
        return character.lower()
    if character.islower():
        return character.upper()

character = input("A Character: ")
print(toggle(character))
