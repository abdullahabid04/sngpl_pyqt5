import requests


get_pressure_out_url = "https://care.iub.edu.pk/sensor/get_pressure/1/1"

response = requests.post(get_pressure_out_url)
data = response.json()
print(data)
