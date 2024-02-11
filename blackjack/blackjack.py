import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(card_list: list):
    total = 0
    for cardNumber in card_list:
        total += cardNumber
    return total


def print_game_final_status(user_card_list: list, computer_card_list: list):
    print(f"Your final hand: {user_card_list}, current score: {calculate_score(user_card_list)}")
    print(f"Computer's final hand: {computer_card_list}, current score: {calculate_score(computer_card_list)}")


def game_status(user_card_list: list, computer_card_list: list, user_choice):
    user_total = calculate_score(user_card_list)
    computer_total = calculate_score(computer_card_list)
    print(f"Your final hand: {userCardDeck}, current score: {calculate_score(userCardDeck)}")
    print(f"Computer's final hand: {computerCardDeck}, current score: {calculate_score(computerCardDeck)}")

    if user_total == 21:
        print("Win with a Blackjack 😎")

    elif computer_total == 21:
        print("Lose, opponent has Blackjack 😱")

    elif user_choice == 'y':
        if user_total > 21:
            print("You went over. You lose 😭")

        elif computer_total > 21:
            print("Opponent went over. You win 😁")

        elif user_total > computer_total:
            print("You win 😃")

        elif user_total < computer_total:
            print("You lose 😤")

        elif computer_total == user_total:
            print("Draw 🙃")


is_continue = True
while is_continue:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
    if choice == 'y':

        print(art.logo)

        userCardDeck = [random.choice(cards) for i in range(0, 2)]
        computerCardDeck = [random.choice(cards) for i in range(0, 2)]

        is_new_card = True

        while is_new_card:
            print(f"Your cards: {userCardDeck}, current score: {calculate_score(userCardDeck)}")
            print(f"Computer's first card: {computerCardDeck[0]}")
            game_status(userCardDeck, computerCardDeck, 'n')

            next_choice = input("Type 'y' to get another card, type 'n' to pass: y : ")

            if next_choice == 'y':
                userCardDeck.append(random.choice(cards))
                computerCardDeck.append(random.choice(cards))
                game_status(userCardDeck, computerCardDeck, 'n')
            else:
                game_status(userCardDeck, computerCardDeck, 'y')
                is_new_card = False

    else:
        is_continue = False
