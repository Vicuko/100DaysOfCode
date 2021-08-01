import requests
from datetime import datetime

MY_LAT = 43.349590
MY_LONG = -3.326350

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)

response.raise_for_status()

data = response.json()
iss_data = data["iss_position"]
longitude = float(iss_data["longitude"])
latitude = float(iss_data["latitude"])
iss_position = (latitude, longitude)
print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)
print(datetime.now().hour)

