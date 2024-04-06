import datetime as dt
import random
import smtplib

current_date = dt.datetime.now()
day_of_week = current_date.weekday()
my_email = "bjayamila@gmail.com"
my_password = "tiok cebn rmyh ovpa"


def send_email():
    with open("quotes.txt", "r") as files:
        quotes = [quote.replace("\n", "") for quote in files.readlines()]

    # connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(my_email, "bethmij@gmail.com", f"Subject:Motivation For the Day\n\n{random.choice(quotes)}")
    connection.close()


if day_of_week == 5:
    send_email()
