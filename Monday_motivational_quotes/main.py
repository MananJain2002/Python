import datetime as dt
from random import choice
import smtplib

MY_EMAIL = "your_mail@gmail.com"
MY_PASSWORD = "your_password"

now = dt.datetime.now()
if now.weekday() == 0:

    with open("./quotes.txt") as f:
        data = f.readlines()
        quote = choice(data)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:

        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="other_mail@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )