import requests


get_demand_url = "https://care.iub.edu.pk/demand/get_demand/1"


response = requests.post(get_demand_url)
data = response.json()
print(data)
