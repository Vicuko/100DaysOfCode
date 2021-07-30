from smtplib import SMTP
import passwords

my_email = "mymail@gmail.com"
password = passwords.GMAIL_PASS

with SMTP(host="smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="receivermail@gmail.com",
                        msg="Subject: Superemail\n\n"
                            "<b>Hello</b>")
    connection.close()