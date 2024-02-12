import random
import art
import game_data

print(art.logo)
total_marks = 0
celebrity_A = random.choice(game_data.data)


def get_follow_most():
    if celebrity_A['follower_count'] > celebrity_B['follower_count']:
        return celebrity_A
    else:
        return celebrity_B


is_continue = True

while is_continue:
    celebrity_B = random.choice(game_data.data)

    while celebrity_A == celebrity_B:
        celebrity_B = random.choice(game_data.data)

    print(f"Compare A: {celebrity_A['name']}, a {celebrity_A['description']}, from {celebrity_A['country']}")
    print(art.vs)
    print(f"Against B: {celebrity_B['name']}, a {celebrity_B['description']}, from {celebrity_B['country']}")
    choice = input("Who has more followers? Type 'A' or 'B' : ")
    winner = get_follow_most()

    if choice == 'A' or choice == 'B':
        if choice == 'A' and winner == celebrity_A or choice == 'B' and winner == celebrity_B:
            total_marks += 1
            celebrity_A = celebrity_B
            print('\n' * 100)
            print(art.logo)
            print(f"You're right! Current Score: {total_marks}")
        else:
            print(f"Sorry, that's wrong. Final Score: {total_marks}")
            is_continue = False
    else:
        is_continue = False
