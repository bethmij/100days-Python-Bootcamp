print("Welcome to the tip calculator")
total = float(input("what was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10,12 or 15? "))
people_count = int(input("How many people to split the bill? "))
pay_total = (total+(total*percentage/100))/people_count
print(f"Each person should pay: ${round(pay_total,2)} ")
