#!/usr/bin/python3
""" Weather Statistics by Barron Stone for Code Clinic: Python """

from csv import DictReader
from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox
import re
import numpy as np
import matplotlib
from PIL import ImageTk, Image
from matplotlib.dates import date2num, num2date
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from Projects.SNGPL.database import *
from Projects.SNGPL.Requirements import *
from Projects.SNGPL.utilities import destroy


class WeatherStatistics:

    def __init__(self, root):
        self.frame = Frame(root, bg=COLORS["BLUE_HEX"])
        self.frame.pack(fill=BOTH, expand=True)

        widget_frame = Frame(self.frame, bg=COLORS["BLUE_HEX"], height=150)
        widget_frame.pack(fill=BOTH, expand=True)

        graph_frame = Frame(self.frame, bg=COLORS["BLUE_HEX"], height=450)
        graph_frame.pack(fill=BOTH, expand=True)

        # datetime_list, pressure_list = [], []
        # datetime_re = re.compile(r'[\d]{2,4}')
        #
        # data = get_dated_pressure(1, "2022-01-14 00:00:00", "2022-01-17 23:59:59")
        # print(data)
        #
        # for i in range(len(data)):
        #     pressure_list.append(data[i]["pressure_value"])
        #     datetime_list.append(date2num(datetime(*list(map(int, datetime_re.findall(data[i]["timestamp"]))))))
        #
        # self.datetime_array = np.array(datetime_list)
        # self.pressure_array = np.array(pressure_list)

        # print(self.datetime_array, "\n", self.pressure_array)

        matplotlib.rc('font', size=18)
        f = Figure()
        f.set_facecolor((0, 0, 0, 0))
        self.a = f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(f, graph_frame)
        self.canvas.draw()
        toolbar_frame = ttk.Frame(graph_frame)  # needed to put navbar above plot
        toolbar = NavigationToolbar2Tk(self.canvas, toolbar_frame)
        toolbar.update()
        toolbar_frame.pack(side=TOP, fill=X, expand=0)
        self.canvas._tkcanvas.pack(fill=BOTH, expand=1)

        self.start = StringVar()
        self.end = StringVar()
        start_date = Entry(widget_frame, width=19, textvariable=self.start, font='Courier 12')
        start_date.place(x=100, y=50)
        end_date = Entry(widget_frame, width=19, textvariable=self.end, font='Courier 12')
        end_date.place(x=200, y=50)

        # self.start.set(str(num2date(self.datetime_array[0]))[0:19])
        # self.end.set(str(num2date(self.datetime_array[-1]))[0:19])

        self._update()

    def _update(self):
        datetime_list, pressure_list = [], []
        datetime_re = re.compile(r'[\d]{2,4}')

        data = get_dated_pressure(1, "2022-01-14 00:00:00", "2022-01-17 23:59:59")
        print(data)

        for i in range(len(data)):
            pressure_list.append(data[i]["pressure_value"])
            datetime_list.append(date2num(datetime(*list(map(int, datetime_re.findall(data[i]["timestamp"]))))))

        datetime_array = np.array(datetime_list)
        pressure_array = np.array(pressure_list)

        self.start.set(str(num2date(datetime_array[0]))[0:19])
        self.end.set(str(num2date(datetime_array[-1]))[0:19])

        start_num = date2num(datetime(*list(map(int, re.findall(r'[\d]{1,4}', self.start.get())))))
        end_num = date2num(datetime(*list(map(int, re.findall(r'[\d]{1,4}', self.end.get())))))

        start_idx = np.searchsorted(datetime_array, start_num)
        end_idx = np.searchsorted(datetime_array, end_num)

        print(start_num, end_num, start_idx, end_idx)

        if end_idx <= start_idx:
            messagebox.showerror(title='Invalid Input Values',
                                 message='End Date must be after Start Date')
            return

        self.a.clear()
        self.a.plot_date(datetime_array[start_idx:end_idx],
                         pressure_array[start_idx:end_idx], linewidth=2)
        self.a.set_ylabel('Pressure')
        self.a.set_xlabel('Date')

        self.canvas.draw()


def main():
    root = Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")

    app = WeatherStatistics(root)

    root.mainloop()


if __name__ == "__main__":
    main()
