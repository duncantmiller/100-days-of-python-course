import requests
from datetime import datetime

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

iss_json = iss_response.json()
print(iss_json)
lat = iss_json["iss_position"]["latitude"]
lng = iss_json["iss_position"]["longitude"]
url_params = f"lat={lat}&lng={lng}&formatted=0"

sun_response = requests.get(url=f"http://api.sunrise-sunset.org/json?{url_params}")
sun_json = sun_response.json()
print(sun_response.json())

sunrise = sun_json["results"]["sunrise"]
sunset = sun_json["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])
time_now = datetime.now()
