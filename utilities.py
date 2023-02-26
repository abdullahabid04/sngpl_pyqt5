from tkinter import *
from tkinter import messagebox
from threading import *
import time
import random
from Projects.SNGPL.database import read_data
from Projects.SNGPL.Requirements import graph_pres, graph_time


def validate(value):
    digit, char = False, False

    if value.isdigit():
        digit = True
    if not(value.isdigit()):
        char = True

    return digit, char


def add_win(n, win1, win2, txt):
    n.add(win1, text=txt)
    n.hide(win2)


def display_label(win, txt, color, font_size, x, y):
    Label(win, text=txt, font=("Times 20", font_size, "bold"), bg="light blue", fg=color).place(x=x, y=y)


def clear(event, entry):
    entry.delete(0, END)


def destroy(event, root):
    root.destroy()


def dummy_function():
    values = []

    for x in range(1000):
        values.append(x)

    print(values)


def get_data(root):
    pass


def threaded_function():
    print("Thread")

    # timer_ = Timer(1.0, timer)
    # timer_.start()
    # timer_.join()


def timer():
    thread = Thread(target=threaded_function)
    thread.start()
    thread.join()

    timer_ = Timer(1.0, timer)
    timer_.start()
    timer_.join()


def start_timer():
    timer_ = Timer(1.0, timer)
    timer_.start()
    timer_.join()


def start_bar(root, progress_bar, percents=None, tasks=None):
    function_1 = lambda: dummy_function()
    function_2 = lambda r=root: get_data(r)
    function_to_call = function_1
    function_count = 25
    total = function_count
    completed = 0
    i, t = 0, 2

    initial_time = time.time()

    while completed < total:
        i += 1

        time_initial = time.time()
        function_to_call()
        time_final = time.time()
        lapse_time = time_final - time_initial

        time.sleep(lapse_time)
        speed = random.random()

        progress_bar['value'] = (completed / total) * 100
        completed += speed

        if percents is not None:
            percents.set(str(int((completed / total) * 100)) + " %")
        if tasks is not None:
            tasks.set(str(int(completed)) + " / " + str(total) + " tasks completed")

        root.update()

    final_time = time.time()
    time_lapse = final_time - initial_time

    print(f"{i} loops in {round(time_lapse, 2)} secs")

    return True
