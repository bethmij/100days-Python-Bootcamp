print("The Love Calculator is calculating your score...")
name1 = input().lower()  # What is your name?
name2 = input().lower()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

true_count = 0
love_count = 0

for name_letter in range(0, len(name1)):
    true_count += 1 if name1[name_letter] in "true" else 0
    love_count += 1 if name1[name_letter] in "love" else 0

for name_letter in range(0, len(name2)):
    true_count += 1 if name2[name_letter] in "true" else 0
    love_count += 1 if name2[name_letter] in "love" else 0


final_count = str(true_count) + str(love_count)

print(f"Your score is {final_count}.")
