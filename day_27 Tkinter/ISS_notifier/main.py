import smtplib
import time
from datetime import datetime
import requests

my_latitude = 6.040200
my_longitude = 80.220642
my_email = "bjayamila@gmail.com"
my_password = "tiok cebn rmyh ovpa"


def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_data = response.json()

    longitude = float(iss_data["iss_position"]["longitude"])
    latitude = float(iss_data["iss_position"]["latitude"])

    if (my_longitude - 5) <= longitude <= (my_longitude + 5) and (my_latitude - 5) <= latitude <= (my_latitude + 5):
        return True


def is_night():
    parameters = {
        "lat": my_latitude,
        "lng": my_longitude,
        "formatted": 0
    }

    response = requests.get('https://api.sunrise-sunset.org/json', parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']

    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    current_hour = datetime.now().hour

    if current_hour <= sunrise_hour or current_hour >= sunset_hour:
        return True


def send_email():
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.starttls()
    conn.login(my_email, my_password)
    conn.sendmail(my_email, "bethmij@gmail.com",
                  "Subject: LOOK UP☝️\n\nThe ISS is above you in the sky")
    conn.close()


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_email()
