class MenuItem:
    def __init__(self, name, water, coffee, milk, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
