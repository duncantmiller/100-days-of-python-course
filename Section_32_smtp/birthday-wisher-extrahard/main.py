##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import os

email = os.environ.get("100_DAYS_EMAIL_ADDRESS")
password = os.environ.get("100_DAYS_EMAIL_PASSWORD")

def get_message():
    """get a random message"""
    number = random.randint(1, 3)
    with open(f"letter_templates/letter_{number}.txt", "r") as file:
        message = file.read()
    return message

def send_email(message, name):
    """send the email"""
    personalized_letter = message.replace('[NAME]', name)
    print(personalized_letter)
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=email, password=password)
    #     connection.sendmail(
    #         from_addr=email, to_addrs="bar@gmail.com", msg="Subject:Happy Birthday!\n\n{quote}"
    #     )

def is_it_monday():
    """checks to see if today is monday"""
    today = dt.datetime.now()
    return True
    #return today.weekday == 1

if is_it_monday():
    send_email(get_message(), "dave")
