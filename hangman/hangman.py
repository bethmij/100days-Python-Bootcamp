import random

word = ["elephant", "manifestation", "applepie"]

chosen_word = random.choice(word)
print(chosen_word)

guessed_letter = input("Guess a letter : ")

for letter in chosen_word:
    print("Right" if letter == guessed_letter else "Wrong")
