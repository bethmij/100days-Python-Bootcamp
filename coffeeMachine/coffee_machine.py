from data import resources
from data import MENU

is_continue = True
profit = 0


def resource_sufficiency(drink_name):
    is_sufficient = True

    for ingredient in resources:

        if drink_name == 'espresso' and ingredient == 'milk':
            MENU[drink_name]['ingredients']['milk'] = 0

        if resources[ingredient] < MENU[drink_name]['ingredients'][ingredient]:
            print(f'Sorry there is not enough {ingredient}.')
            is_sufficient = False

    return is_sufficient


def get_money(drink_name):
    print('Please insert coins')
    quarters = int(input('How many quarters : '))
    dimes = int(input('How many dimes : '))
    nickles = int(input('How many nickles : '))
    pennies = int(input('How many pennies : '))

    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    if total < MENU[drink_name]['cost']:
        print("Sorry that's not enough money. Money refunded")
        return total, False
    else:
        return total, True


def transaction(drink_name, cost, amount_spend):

    for ingredient in resources:
        if drink_name == 'espresso' and ingredient == 'milk':
            resources['milk'] -= 0
        else:
            resources[ingredient] -= MENU[drink_name]['ingredients'][ingredient]

    price = MENU[drink_name]['cost']
    cost += price
    balance_amount = amount_spend - price
    return cost, balance_amount


while is_continue:

    choice = input("What would you like? (espresso/latte/cappuccino) : ").lower()

    drinks = ["espresso", "latte", "cappuccino"]

    if choice in drinks:
        is_sufficiency = resource_sufficiency(choice)
        if is_sufficiency:
            spend_amount, is_enough_money = get_money(choice)
            if is_enough_money:
                profit, balance = transaction(choice, profit, spend_amount)
                print(f"Here is ${balance} in change\nHere is your {choice}☕ Enjoy!")

    elif choice == 'report':
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\n"
              f"Coffee: {resources['coffee']}\nMoney: ${profit}")

    elif choice == 'off':
        is_continue = False
