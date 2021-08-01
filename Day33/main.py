import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)

response.raise_for_status()

data = response.json()
iss_data = data["iss_position"]
longitude = iss_data["longitude"]
latitude = iss_data["latitude"]
iss_position = (latitude, longitude)
print(iss_position)