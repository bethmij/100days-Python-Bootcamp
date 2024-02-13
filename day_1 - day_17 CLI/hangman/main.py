import random

import hangman_word
import hangman_logo

print(hangman_logo.logo)

chosen_word = random.choice(hangman_word.word_list)

word_list = ["_" for i in chosen_word]
lives = 6

end_of_game = False

while not end_of_game:

    print(''.join(word_list))
    wrong_count = 0

    print(hangman_logo.stages[lives])

    guessed_letter = input("Guess a letter : ")

    if guessed_letter in word_list:
        print(f"You already guessed {guessed_letter}")
        continue

    for index, letter in enumerate(chosen_word):
        if letter == guessed_letter.lower():
            word_list[index] = letter
        else:
            wrong_count += 1

    if wrong_count == len(chosen_word):
        lives -= 1
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")

    if "_" not in word_list:
        print("You Won!")
        end_of_game = True
    elif lives == 0:
        print("You Lose!")
        end_of_game = True


