import requests


get_pressure_in_url = "https://care.iub.edu.pk/sensor/get_pressure/1/0"

response = requests.post(get_pressure_in_url)
data = response.json()
print(data)
