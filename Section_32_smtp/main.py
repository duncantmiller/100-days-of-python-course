import smtplib
import datetime as dt
import random

email = "foo@gmail.com"
password = "bar"

def get_quote():
    """get a quote from the file"""
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
    return random.choice(quotes)

def send_email(quote):
    """send the email"""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="bar@gmail.com", msg="Subject:hi\n\n{quote}")

def is_it_monday():
    """checks to see if today is monday"""
    today = dt.datetime.now()
    return today.weekday == 0

if is_it_monday():
    send_email(get_quote)
