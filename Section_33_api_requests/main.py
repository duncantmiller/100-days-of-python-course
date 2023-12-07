import requests
from datetime import datetime
import time

MY_LATITUDE = 45.51481
MY_LONGITUDE = -122.68427

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

iss_json = iss_response.json()
iss_latitude = float(iss_json["iss_position"]["latitude"])
iss_longitude = float(iss_json["iss_position"]["longitude"])

def parameters():
    return {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    }

def sun_response_hour(value):
    return int(sun_json()["results"][value].split("T")[1].split(":")[0])

def sun_json():
    sun_response = requests.get(url=f"http://api.sunrise-sunset.org/json?", params=parameters())
    sun_response.raise_for_status()
    return sun_response.json()

while True:
    current_hour = datetime.now().hour
    if current_hour > sun_response_hour("sunset") and current_hour < sun_response_hour("sunrise"):
        if abs(iss_latitude - MY_LATITUDE) < 5 and abs(iss_longitude - MY_LONGITUDE) < 5:
            print("Look up!")
    else:
        print("Don't look up.")
    time.sleep(60)
