import requests
from datetime import datetime

MY_LATITUDE = 45.51481
MY_LONGITUDE = -122.68427

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

iss_json = iss_response.json()
print(iss_json)
iss_latitude = iss_json["iss_position"]["latitude"]
iss_longitude = iss_json["iss_position"]["longitude"]

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}

sun_response = requests.get(url=f"http://api.sunrise-sunset.org/json?", params=parameters)
sun_json = sun_response.json()
print(sun_response.json())

sunrise = sun_json["results"]["sunrise"]
sunset = sun_json["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])
time_now = datetime.now()
