import random

word = ["elephant", "manifestation", "applepie"]

chosen_word = random.choice(word)
print(chosen_word)
word_list = ["_" for i in chosen_word]

end_of_game = False

while not end_of_game:
    guessed_letter = input("Guess a letter : ")

    for index, letter in enumerate(chosen_word):
        if letter == guessed_letter.lower():
            word_list[index] = letter
    print(word_list)

print("You Won!")
