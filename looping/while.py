'''i = 8
count = 0
while i <= 10:
    print(i)
    count += 1
    i += 1
print("The while loop ran", count , "times")''' 

#guessing game
secret_word = "car"
guess_word = ""
guess_count = 1
guess_limit = 3
out_of_guesses = False

while guess_word != secret_word and not(out_of_guesses):
    guess_word = input("Enter the secret word: ")
    guess_count += 1
    if guess_count > guess_limit:
        out_of_guesses = True
if guess_word == secret_word:
    print("You win")
elif out_of_guesses:
    print("You ran out of guesses")

