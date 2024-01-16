import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list = [rock, paper, scissors]
your_choice = 0

while True:
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors : ")
    if choice == "1" or choice == "2" or choice == "3":
        your_choice = int(choice)
        print(choice_list[your_choice])

        rand_number = random.randint(0, 2)
        print("Computer chose :")
        print(choice_list[rand_number])

        if your_choice == rand_number:
            print("Draw! Let's try again")
            continue
        elif (your_choice == 0 and rand_number == 2) or (your_choice == 1 and rand_number == 0) or (
                your_choice == 2 and rand_number == 1):
            print("You Win!")
            break
        else:
            print("You Loose!")
            break
    else:
        print("Invalid Input! Please Try Again")
