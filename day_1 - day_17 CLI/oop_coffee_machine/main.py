from menu import Menu
from moneyMachine import MoneyMachine
from coffeeMaker import CoffeeMaker

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
drinks = ["espresso", "latte", "cappuccino"]

is_continue = True
while is_continue:

    choice = input("What would you like? (espresso/latte/cappuccino) : ").lower()

    if choice in drinks:
        drink = menu.find_drink(choice)
        is_sufficiency = coffee_maker.is_resource_sufficient(drink)
        if is_sufficiency:
            money_accepted = money_machine.make_payment(drink.cost)
            if money_accepted:
                coffee_maker.make_coffee(drink)

    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()

    elif choice == 'off':
        is_continue = False
