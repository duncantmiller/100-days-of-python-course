import requests
from datetime import datetime
import time

MY_LATITUDE = 45.51481
MY_LONGITUDE = -122.68427

def iss_json():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    return iss_response.json()

def iss_latitude():
    return float(iss_json()["iss_position"]["latitude"])

def iss_longitude():
    return float(iss_json["iss_position"]["longitude"])

def parameters():
    return {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    }

def my_hour_of(value):
    return int(sun_json()["results"][value].split("T")[1].split(":")[0])

def sun_json():
    sun_response = requests.get(url=f"http://api.sunrise-sunset.org/json?", params=parameters())
    sun_response.raise_for_status()
    return sun_response.json()

def current_hour():
    return datetime.now().hour

while True:
    if current_hour() > my_hour_of("sunset") and current_hour() < my_hour_of("sunrise"):
        if abs(iss_latitude() - MY_LATITUDE) < 5 and abs(iss_longitude() - MY_LONGITUDE) < 5:
            print("Look up!")
    else:
        print("Don't look up.")
    time.sleep(60)
