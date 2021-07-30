##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
from pathlib import Path
import random
from smtplib import SMTP
import passwords

MY_EMAIL = "sender@gmail.com"
MY_PASSWORD = passwords.GMAIL_PASS
# 1. Update the birthdays.csv
# DONE
# 2. Check if today matches a birthday in the birthdays.csv
def check_birthdays():
    now = dt.datetime.now()
    year, month, day = now.year, now.month, now.day

    try:
        birthdays_data = pd.read_csv("birthdays.csv")
    except FileNotFoundError:
        print("There is no csv")
    else:
        for index,row in birthdays_data.iterrows():
            if row.month == month and row.day == day:
                # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
                letter = create_letter(name=row["name"], age=(year - row["year"]))
                # 4. Send the letter generated in step 3 to that person's email address.
                send_mail(letter, email=row["email"])

def create_letter(name, age):
    letter = get_random_letter()
    letter = letter.replace("[NAME]", name)
    return letter

def get_random_letter():
    p = Path('./letter_templates')
    possible_letters = list(p.glob('*'))
    random_letter = random.choice(possible_letters)
    letter_content = ""
    try:
        with open(random_letter) as template_letter:
            letter_content = template_letter.read()
    except FileNotFoundError:
        print("It seems the file was just deleted")
    finally:
        return letter_content

def send_mail(content,  email, subject="Happy Birthday!"):
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=f"{email}",
                            msg=f"Subject: {subject}\n\n"
                                f"{content}")

check_birthdays()




