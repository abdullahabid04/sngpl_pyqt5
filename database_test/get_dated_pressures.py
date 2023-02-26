import requests


get_dated_pressures_url = "https://care.iub.edu.pk/sensor/get_dated_pressures"
get_dated_pressures_url_object = {"sid": "1", "start": "2021-01-14 00:00:00", "end": "2021-01-16 23:59:59"}

response = requests.post(get_dated_pressures_url, data=get_dated_pressures_url_object)
data = response.json()
print(data)
