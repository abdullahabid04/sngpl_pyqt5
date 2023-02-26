from tkinter import messagebox
import re
from datetime import datetime
import numpy as np
from matplotlib.dates import date2num, num2date
from Projects.SNGPL.SiteScreen import SiteScreen
from Projects.SNGPL.database import get_dated_pressure, read_data, write_data
from Projects.SNGPL.utilities import validate
from Projects.SNGPL.Requirements import *


def login(root, screen, user, email, password, imgs, open_main):
    if user.get() == admin:
        if email.get() == email_admin and password.get() == password_admin:
            messagebox.showinfo("Administrator", "You are now logged in Administrator")
        else:
            messagebox.showwarning("Administrator", "Your password or email is incorrect")
    elif user.get() == calib:
        if email.get() == email_calibrator and password.get() == password_calibrator:
            messagebox.showinfo("Calibrator", "You are now logged in Calibrator")
        else:
            messagebox.showwarning("Calibrator", "Your password or email is incorrect")
    elif user.get() == oper:
        if email.get() == email_operator and password.get() == password_operator:
            site_screen = SiteScreen(root, frame=screen, imgs=imgs)
            btns = site_screen.buttons
            ent = site_screen.entries
            cmds = [lambda r=root, s=site_screen.frame: open_main(r, s, imgs, site_screen.destroy()),
                    lambda t=site_screen.sid, p=site_screen.pressure: update(t, p),
                    lambda sid=site_screen.sid, sd=site_screen.start, ed=site_screen.end, plt=site_screen.subplot, cnv=site_screen.canvas: plot_graph(sid, sd, ed, plt, cnv),
                    lambda sid=site_screen.sid, in_p=site_screen.in_pressure, out_p=site_screen.out_pressure: data_read(sid, in_p, out_p)
                    ]
            for i in range(len(btns)):
                btns[i]["command"] = cmds[i]
        else:
            messagebox.showwarning("Operator", "Your password or email is incorrect")
    else:
        messagebox.showerror("Invalid Option", "You entered an invalid option")


def update(station_id, pressure):
    tbs = str(station_id.get())
    press = str(pressure.get())

    digit1, char1 = validate(press)
    digit2, char2 = validate(tbs)

    if (digit1 is True and char1 is False) and (digit2 is True and char2 is False):
        try:
            data = write_data(tbs, press)
            success = data["success"]
            if success == 1:
                messagebox.showinfo("Operation Successful", "Pressure has successfully been updated")
            else:
                messagebox.showerror("Operation UnSuccessful", "Oops! Something went Wrong. Please try again later")
        except Exception as e:
            print(e)
    else:
        messagebox.showerror("Invalid Data", "Please enter valid data")


def plot_graph(st_id, start_date, end_date, plot, canvas):
    sid = str(st_id.get())
    start = str(start_date.get())
    end = str(end_date.get())

    data = get_dated_pressure(sid, start, end)
    print(data)

    in_datetime_list, out_datetime_list, in_pressure_list, out_pressure_list = [], [], [], []
    datetime_re = re.compile(r'[\d]{2,4}')

    for i in range(len(data)):
        if data[i]["flag"] == '0':
            in_datetime_list.append(date2num(datetime(*list(map(int, datetime_re.findall(data[i]["timestamp"]))))))
            in_pressure_list.append(float(data[i]["pressure_value"]))
        if data[i]["flag"] == '1':
            out_datetime_list.append(date2num(datetime(*list(map(int, datetime_re.findall(data[i]["timestamp"]))))))
            out_pressure_list.append(float(data[i]["pressure_value"]))

    in_datetime_array = np.array(in_datetime_list)
    out_datetime_array = np.array(out_datetime_list)
    in_pressure_array = np.array(in_pressure_list)
    out_pressure_array = np.array(out_pressure_list)

    start_date_in = str(num2date(in_datetime_array[0]))[0:19]
    end_date_in = str(num2date(in_datetime_array[-1]))[0:19]

    start_num_in = date2num(datetime(*list(map(int, re.findall(r'[\d]{1,4}', start_date_in)))))
    end_num_in = date2num(datetime(*list(map(int, re.findall(r'[\d]{1,4}', end_date_in)))))

    start_idx_in = np.searchsorted(in_datetime_array, start_num_in)
    end_idx_in = np.searchsorted(in_datetime_array, end_num_in)

    start_date_out = str(num2date(out_datetime_array[0]))[0:19]
    end_date_out = str(num2date(out_datetime_array[-1]))[0:19]

    start_num_out = date2num(datetime(*list(map(int, re.findall(r'[\d]{1,4}', start_date_out)))))
    end_num_out = date2num(datetime(*list(map(int, re.findall(r'[\d]{1,4}', end_date_out)))))

    start_idx_out = np.searchsorted(out_datetime_array, start_num_out)
    end_idx_out = np.searchsorted(out_datetime_array, end_num_out)

    plot.clear()
    plot.plot_date(in_datetime_array[start_idx_in:end_idx_in],
                   in_pressure_array[start_idx_in:end_idx_in],
                   'b', label="In-pressure", linestyle="dashed")

    plot.plot_date(out_datetime_array[start_idx_out:end_idx_out],
                   out_pressure_array[start_idx_out:end_idx_out],
                   'r', label="Out-pressure", linestyle="dashed")

    plot.legend(loc="upper right", prop={"size": 7})

    plot.set_ylabel('Pressure')
    plot.set_xlabel('Date')

    canvas.draw()


def data_read(tbs, in_pressure, out_pressure):
    sid = str(tbs.get())

    d1, d2 = read_data(sid)

    pressure_in = d1["value"]
    pressure_out = d2["value"]

    in_pressure.set(str(pressure_in))
    out_pressure.set(str(pressure_out))


def unused_function():
    messagebox.showinfo("Function Call", "Function called on Button pressed")
