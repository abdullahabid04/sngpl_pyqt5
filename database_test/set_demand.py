import requests


set_demand_url = "https://care.iub.edu.pk/demand/set_demand/1/100"


response = requests.post(set_demand_url)
data = response.json()
print(data)
