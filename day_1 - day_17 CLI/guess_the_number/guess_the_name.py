import random


def guess_number(attempts: int):
    for i in range(attempts):
        print(f"You have {attempts - i} attempts remaining to guess the number")
        guessed_number = int(input("Make a guess : "))

        if number == guessed_number:
            return f"You got it! The answer was {number}"

        elif number < guessed_number:
            print("Too high. Guess again")

        elif number > guessed_number:
            print("Too low. Guess again")

    return f"You've run out of guesses, you lose!"


print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
number = random.randint(1, 100)
print(number)

if difficulty_level == 'easy':
    print(guess_number(10))

elif difficulty_level == 'hard':
    print(guess_number(5))
