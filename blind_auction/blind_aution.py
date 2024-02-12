import art
import os

print(art.logo)
print("Welcome to the secret auction program")


def calculate_max(bid_detail):
    """
    Calculate max bid with winner name
    :param bid_detail:
    :return: winner and maximum bid
    """
    max_num = 0
    winner = ""

    for key in bid_detail:
        bid_num = int(bid_detail[key])
        if bid_num > max_num:
            max_num = bid_num
            winner = key

    return winner, max_num


is_End = False
bid_details = {}

while not is_End:
    name = input("What's your name? : ")
    bid = input("What's your bid : $")
    choice = input("Are there any other bidders. Type 'yes' or 'no' : ")

    bid_details[name] = bid

    if choice == "yes":
        os.system('cls')
        continue
    elif choice == "no":
        name, max_bid = calculate_max(bid_details)
        print(f"The winner is {name} with a bid of ${max_bid}")
        is_End = True
    else:
        print("Invalid Input! Try Again")
        continue
