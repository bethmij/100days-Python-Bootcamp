import random
import smtplib
import datetime
import pandas

current_date = datetime.datetime.today()
current_month = current_date.month
current_day = current_date.day
my_email = "bjayamila@gmail.com"
my_password = "tiok cebn rmyh ovpa"


def send_email(sending_email, subject, message):
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.starttls()
    conn.login(my_email, my_password)
    conn.sendmail(my_email, sending_email, f"Subject: {subject}\n\n{message}")
    conn.close()


def birthday_wish_letter(name):
    random_num = random.randint(1, 3)
    with open(f"letter_templates/letter_{random_num}.txt") as files:
        letter = [file.replace("[NAME]", name) for file in files.readlines()]
        return letter


try:
    with open("birthdays.csv", "r") as file:
        birthdays = pandas.read_csv(file).to_dict(orient="records")

except FileNotFoundError:
    print("No File Found")

else:
    for birthday in birthdays:
        if birthday['month'] == current_month and birthday['day'] == current_day:
            sending_email = birthday['email']
            print(sending_email)
            message = birthday_wish_letter(birthday['name'])
            send_email(sending_email, "Happy Birthday!", message)
