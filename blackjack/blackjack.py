import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game_status(user_card_list: list, computer_card_list: list):
    user_total = sum(user_card_list)
    computer_total = sum(computer_card_list)

    if user_total == 21 and len(user_card_list) == 2:
        return "Win with a Blackjack 😎"

    elif computer_total == 21 and len(computer_card_list) == 2:
        return "Lose, opponent has Blackjack 😱"

    elif user_total > 21:
        return "You went over. You lose 😭"

    elif computer_total > 21:
        return "Opponent went over. You win 😁"

    elif user_total > computer_total:
        return "You win 😃"

    elif user_total < computer_total:
        return "You lose 😤"

    elif computer_total == user_total:
        return "Draw 🙃"


is_continue = True
while is_continue:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
    if choice == 'y':
        print(art.logo)

        userCardDeck = [random.choice(cards) for i in range(2)]
        computerCardDeck = [random.choice(cards) for i in range(2)]
        is_new_card = True

        while is_new_card:

            user_score = sum(userCardDeck)
            computer_score = sum(computerCardDeck)

            print(f"Your cards: {userCardDeck}, current score: {user_score}")
            print(f"Computer's first card: {computerCardDeck[0]}")

            if user_score >= 21 or computer_score >= 21:
                is_new_card = False

            else:
                next_choice = input("Type 'y' to get another card, type 'n' to pass: y : ")

                if next_choice == 'y':
                    userCardDeck.append(random.choice(cards))

                    if userCardDeck[-1] == 11 and user_score > 21:
                        userCardDeck[-1] = 1

                    while computer_score < 17:
                        computerCardDeck.append(random.choice(cards))
                        computer_score = sum(computerCardDeck)

                else:
                    is_new_card = False

        print(f"Your final hand: {userCardDeck}, current score: {sum(userCardDeck)}")
        print(f"Computer's final hand: {computerCardDeck}, current score: {sum(computerCardDeck)}")
        print(game_status(userCardDeck, computerCardDeck))

    else:
        is_continue = False

