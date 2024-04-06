import smtplib

my_email = "bjayamila@gmail.com"
my_password = "tiok cebn rmyh ovpa"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="bethmij@gmail.com", msg=f"Subject:Hello")
connection.close()