import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

word = ["elephant", "manifestation", "applepie"]

print(logo)

chosen_word = random.choice(word)
print(chosen_word)
word_list = ["_" for i in chosen_word]
lives = 6

end_of_game = False
wrong_count = 0

while not end_of_game:
    print(''.join(word_list))

    # print(stages[lives])
    print(lives)

    guessed_letter = input("Guess a letter : ")

    for index, letter in enumerate(chosen_word):
        if letter == guessed_letter.lower():
            word_list[index] = letter
        else:
            wrong_count += 1

    if wrong_count == len(chosen_word):
        lives -= 1
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")

    if "_" not in word_list or lives == 0:
        print("You Lose!")
        end_of_game = True

print("You Won!")
