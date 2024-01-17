import art

print(art.logo)
operator = ["+", "-", "*", "/"]
is_start_new = False
is_continue = False

while not is_start_new:
    num1 = input("What's the first number? : ")

    for op in operator:
        print(op)

    operator_choice = input("Pick an operator : ")

    if operator_choice in operator:
        while not is_continue:
            num2 = input("What's the second number? : ")
            cal_num = "{:.1f}".format(eval(num1 + operator_choice + num2))

            print(f"{num1} + {num2} = {cal_num}")
            option = input(f"Type 'y' to continue calculating with {cal_num} or type 'n' to start new calculation : ")

            if option.lower() == "y":
                num1 = cal_num
                continue
            elif option.lower() == "n":
                break
    else:
        print("Invalid Input! Try Again")
