print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroad = input('You\'re at a crossroad. Where you wanna go? Type "left" or "right" : ')

if crossroad.lower() == "left":
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake. '
                 'Type "wait" to wait for a boot. Type "swim" to swim across. : ')
    if lake.lower() == "wait":
        color = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, onr yellow and one blue. "
            "Which color do you choose? :")
        if color.lower() == "red":
            print("It's a room full of fire. GAME OVER!")
        elif color.lower() == "yellow":
            print("You found the treasure! YOU WIN!")
        elif color.lower() == "blue":
            print("You enter a room of beasts. GAME OVER!")
        else:
            print("Invalid input! GAME OVER!")
    else:
        print("You got attacked by a angry trout. GAME OVER!")
else:
    print("You fell into a hole. GAME OVER!")
