##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import os
import pandas

from_email = os.environ.get("100_DAYS_EMAIL_ADDRESS")
password = os.environ.get("100_DAYS_EMAIL_PASSWORD")

def matching_birthdays():
    """find matching birthdays"""
    data = pandas.read_csv("birthdays.csv")
    data_frame = pandas.DataFrame(data)
    today = dt.datetime.now().date()
    # Convert the year, month, and day columns to a datetime column
    data_frame['date'] = pandas.to_datetime(data_frame[['year', 'month', 'day']])

    # Filter the DataFrame based on the target date
    matching_records = data_frame[data_frame['date'].dt.date == today]

    return matching_records.values

def get_message():
    """get a random message"""
    number = random.randint(1, 3)
    with open(f"letter_templates/letter_{number}.txt", "r") as file:
        message = file.read()
    return message

def send_email(message, name, to_email):
    """send the email"""
    personalized_letter = message.replace('[NAME]', name)
    print(personalized_letter)
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=from_email, password=password)
    #     connection.sendmail(
    #         from_addr=from_email, to_addrs=to_email, msg="Subject:Happy Birthday!\n\n{quote}"
    #     )

print(matching_birthdays())
for birthday in matching_birthdays():
    send_email(get_message(), name=birthday[0], to_email=birthday[1])
