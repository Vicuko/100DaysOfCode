from smtplib import SMTP
import passwords
import datetime as dt
import random
#
my_email = "sender@gmail.com"
password = passwords.GMAIL_PASS


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    try:
        with open("quotes.txt") as quotes_file:
            content = quotes_file.readlines()
            random_quote = random.choice(content)
            print(random_quote)
    except FileNotFoundError as error_message:
        print(error_message)
    else:
        with SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="receiver@gmail.com",
                                msg="Subject: Motivation Mail\n\n" +
                                    str(random_quote))
