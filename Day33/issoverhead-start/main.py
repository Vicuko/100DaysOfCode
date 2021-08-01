import time
import requests
from datetime import datetime
from smtplib import SMTP
import passwords

MY_LAT = 43.349590
MY_LONG = -3.326350
MARGIN = 5
MY_MAIL = passwords.MY_MAIL
RECEIVER = passwords.RECEIVER
MY_PASS = passwords.GMAIL_PASS

def get_ISS_location():
    '''Return ISS current longitude and location in the form of a tuple: (longitude, latitude)'''
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (iss_longitude, iss_latitude)

#Your position is within +5 or -5 degrees of the ISS position.

def get_suntime(longitude, latitude):
    '''Get sunrise and sunset times for given location in the form of longitude, latitude'''
    parameters = {
        "lat": latitude,
        "lng": longitude,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return (sunrise, sunset)

def is_night(sunrise, sunset):
    current_hour = datetime.now().hour
    if current_hour >= sunset or current_hour <= sunrise:
        return True
    return False

def is_iss_overhead():
    iss_lng, iss_lat = get_ISS_location()
    if MY_LONG - 5 <= -iss_lng <= MY_LONG + 5 and MY_LAT - 5 <= iss_lat <= MY_LAT + 5:
        return True
    return False

def send_look_up_mail():
    with SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=RECEIVER, msg="Subject:Look up to the sky!\n\n"
                                                                      "Hey, the ISS is over the sky and it's dark. Take a look!!")
def check_ISS_proximity():
    if is_iss_overhead():
        sunrise, sunset = get_suntime(MY_LONG, MY_LAT)
        if is_night(sunrise, sunset):
            send_look_up_mail()
            return (True)
    else:
        print("It's not dark or close")
        return (False)

# Check every minute if the ISS is above and it's dark:
ISS_is_close = False
while not ISS_is_close:
    ISS_is_close = check_ISS_proximity()
    time.sleep(60)
