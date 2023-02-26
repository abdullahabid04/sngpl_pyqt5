import requests


def read_data(tbs):
    sid = str(tbs)

    get_pressure_in_url = f"https://care.iub.edu.pk/sensor/get_pressure/{sid}/0"
    get_pressure_out_url = f"https://care.iub.edu.pk/sensor/get_pressure/{sid}/1"

    r1 = requests.post(get_pressure_in_url)
    r2 = requests.post(get_pressure_out_url)

    d1 = r1.json()
    d2 = r2.json()

    return d1, d2


def write_data(tbs, pres_val):
    sid = str(tbs)
    pressure = str(pres_val)

    set_demand_url = f"https://care.iub.edu.pk/demand/set_demand/{sid}/{pressure}"

    response = requests.post(set_demand_url)
    data = response.json()

    return data


def get_dated_pressure(tbs_id, start_date, end_date):
    get_dated_pressures_url = "https://care.iub.edu.pk/sensor/get_dated_pressures"
    get_dated_pressures_url_object = {"sid": str(tbs_id), "start": str(start_date), "end": str(end_date)}

    req = requests.post(get_dated_pressures_url, data=get_dated_pressures_url_object)
    data = req.json()[0]

    return data
