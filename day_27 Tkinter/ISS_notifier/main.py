import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

iss_data = response.json()

longitude = iss_data["iss_position"]["longitude"]
latitude = iss_data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
