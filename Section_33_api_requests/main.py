import requests
from datetime import datetime
import time

MY_LATITUDE = 45.51481
MY_LONGITUDE = -122.68427

def iss_json():
    """returns json of iss response"""
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    return iss_response.json()

def iss_latitude():
    """iss latitude"""
    return float(iss_json()["iss_position"]["latitude"])

def iss_longitude():
    "iss longitude"
    return float(iss_json["iss_position"]["longitude"])

def parameters():
    """params for sun api"""
    return {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    }

def my_hour_of(value):
    """gets the hour value from the sun response"""
    return int(sun_json()["results"][value].split("T")[1].split(":")[0])

def sun_json():
    """returns json of sun response"""
    sun_response = requests.get(url=f"http://api.sunrise-sunset.org/json?", params=parameters())
    sun_response.raise_for_status()
    return sun_response.json()

def current_hour():
    """current hour"""
    return datetime.now().hour

def is_night():
    """checks to see if it is currently after sunset or before sunrise"""
    return current_hour() > my_hour_of("sunset") and current_hour() < my_hour_of("sunrise")

def is_iss_near():
    """checks to see if the iss is within 5 degrees of our position"""
    abs(iss_latitude() - MY_LATITUDE) < 5 and abs(iss_longitude() - MY_LONGITUDE) < 5

while True:
    if is_night() and is_iss_near():
        print("Look up!")
    else:
        print("Don't look up.")
    time.sleep(60)
