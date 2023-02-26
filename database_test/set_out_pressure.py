import requests


set_pressure_out_url = "https://care.iub.edu.pk/sensor/set_pressure/1/1/200"


response = requests.post(set_pressure_out_url)
data = response.json()
print(data)

