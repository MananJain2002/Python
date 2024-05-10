import datetime as dt
from random import randint
import pandas as pd
import smtplib

# Set your email and password
MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "yourpassword"

# Get the current date
now = dt.datetime.now()
day = now.day
month = now.month

# Read the birthdays data from a CSV file
data = pd.read_csv("./birthdays.csv")
data = data.to_dict(orient="records")

# Iterate over each birthday person in the data
for birthday_person in data:
    # Check if it's the birthday of the current person
    if birthday_person["month"] == month and birthday_person["day"] == day:
        # Choose a random letter template and replace the placeholder with the person's name
        with open(f"./letter_templates/letter_{randint(1, 3)}.txt") as letter_file:
            contents = "".join(letter_file.readlines())
            contents = contents.replace("[NAME]", birthday_person["name"])
        
        # Connect to the SMTP server and send the birthday email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )
