import requests


set_demand_url = "https://care.iub.edu.pk/demand/set_demand/1/100"
get_demand_url = "https://care.iub.edu.pk/demand/get_demand/1"

set_pressure_in_url = "https://care.iub.edu.pk/sensor/set_pressure/1/0/100"
set_pressure_out_url = "https://care.iub.edu.pk/sensor/set_pressure/1/1/100"

get_pressure_in_url = "https://care.iub.edu.pk/sensor/get_pressure/1/0"
get_pressure_out_url = "https://care.iub.edu.pk/sensor/get_pressure/1/1"

get_dated_pressures_url = "https://care.iub.edu.pk/sensor/get_dated_pressures"
get_dated_pressures_url_object = {"sid": "1", "start": "2022-01-14 00:00:00", "end": "2022-01-17 23:59:59"}

# ======================= only for get_dated_pressures_url =============================
# response = requests.post(get_dated_pressures_url, data=get_dated_pressures_url_object)
# data = response.json()
# print(data)
# =====================================================================================

# ============================ for all the others =====================================
# response = requests.post(set_demand_url)
# data = response.json()
# print(data)
# =====================================================================================
