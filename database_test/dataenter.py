import requests
import time
import random
import threading


def enter_data():
    print("Updating In Pressure")

    initial_time_in = time.time()
    pressure_in = random.randint(90, 100)
    set_pressure_in_url = f"https://care.iub.edu.pk/sensor/set_pressure/1/0/{pressure_in}"

    try:
        req1 = requests.post(set_pressure_in_url)
        if req1.ok:
            if req1.status_code == 200:
                res1 = req1.json()
                if res1["success"] == "1":
                    print("In Pressure Updated")
    except Exception as e:
        print(e)

    final_time_in = time.time()
    time_lapse_in = final_time_in - initial_time_in
    time.sleep(time_lapse_in)

    print("Updating Out Pressure")

    initial_time_out = time.time()
    pressure_out = random.randint(103, 108)
    set_pressure_out_url = f"https://care.iub.edu.pk/sensor/set_pressure/1/1/{pressure_out}"

    try:
        req2 = requests.post(set_pressure_out_url)
        if req2.ok:
            if req2.status_code == 200:
                res2 = req2.json()
                if res2["success"] == "1":
                    print("Out Pressure Updated")
    except Exception as e:
        print(e)

    final_time_out = time.time()
    time_lapse_out = final_time_out - initial_time_out
    time.sleep(time_lapse_out)


def thread_function():
    thread = threading.Thread(target=enter_data)
    thread.start()
    thread.join()

    timer = threading.Timer(60.0, thread_function)
    timer.start()
    timer.join()


if __name__ == "__main__":
    thread_function()
