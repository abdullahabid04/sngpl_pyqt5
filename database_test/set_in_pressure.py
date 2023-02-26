import requests


set_pressure_in_url = "https://care.iub.edu.pk/sensor/set_pressure/1/0/150"


response = requests.post(set_pressure_in_url)
data = response.json()
print(data)
