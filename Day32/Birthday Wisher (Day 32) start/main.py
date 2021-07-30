# from smtplib import SMTP
# import passwords
#
# my_email = "mymail@gmail.com"
# password = passwords.GMAIL_PASS
#
# with SMTP(host="smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="receivermail@gmail.com",
#                         msg="Subject: Superemail\n\n"
#                             "<b>Hello</b>")
#     connection.close()

import datetime as dt

time_now = dt.datetime.now()
year = time_now.year
month = time_now.month
# Day of the week (1-7):
weekday = time_now.weekday()
print(type(time_now))

date_of_birth = dt.datetime(day=1, month=6, year=1987, hour=1)
print(date_of_birth)
