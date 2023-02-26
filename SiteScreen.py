from tkinter import *
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from datetime import datetime
from Projects.SNGPL.utilities import clear
from Projects.SNGPL.Requirements import COLORS, FONT_STYLE


class SiteScreen:
    def __init__(self, root, frame=None, imgs=None) -> None:
        if frame is not None:
            frame.destroy()

        self.frame = Frame(root, bg=COLORS["BLUE_HEX"])
        self.frame.pack(fill=BOTH, expand=True)

        widget_frame = Frame(self.frame, bg=COLORS["BLUE_HEX"], height=150)
        widget_frame.pack(fill=BOTH, expand=True)

        graph_frame = Frame(self.frame, bg=COLORS["BLUE_HEX"], height=450)
        graph_frame.pack(fill=BOTH, expand=True)

        matplotlib.rc('font', size=8)
        figure = Figure()
        figure.set_facecolor((0, 0, 0, 0))

        self.subplot = figure.add_subplot(111)

        self.subplot.spines['top'].set_visible(False)
        self.subplot.spines['right'].set_visible(False)
        self.subplot.spines['bottom'].set_visible(True)
        self.subplot.spines['left'].set_visible(True)

        self.subplot.spines['bottom'].set_color('#1e1953')
        self.subplot.spines['left'].set_color('#1e1953')
        self.subplot.spines['top'].set_color('#1e1953')
        self.subplot.spines['right'].set_color('#1e1953')

        self.subplot.tick_params(axis='x', colors='#1e1953')
        self.subplot.tick_params(axis='y', colors='#1e1953')

        self.canvas = FigureCanvasTkAgg(figure, graph_frame)
        self.canvas.draw()

        toolbar_frame = ttk.Frame(graph_frame)
        toolbar = NavigationToolbar2Tk(self.canvas, toolbar_frame)
        toolbar.update()
        toolbar_frame.pack(side=TOP, fill=X, expand=False)

        self.canvas._tkcanvas.pack(fill=BOTH, expand=True)

        image = Label(widget_frame, image=imgs[0], bg=COLORS["BLUE_HEX"])
        image.pack()
        image.place(x=10, y=42)

        txt = ["name", "site", "TBS", "last updated", "start time", "end time", "status", "alarm", "pressure"]
        self.entries = []
        lx, ly = [90, 340, 590, 90, 340, 590, 90, 340, 590], [20, 20, 20, 60, 60, 60, 100, 100, 100]
        ex, ey = [190, 440, 690, 190, 440, 690, 190, 440, 690], [20, 20, 20, 60, 60, 60, 100, 100, 100]

        for i in range(len(txt)):
            lbl = Label(widget_frame, text=txt[i], bg=COLORS["BLUE_HEX"], fg=COLORS["DARK_BLUE"],
                        font=(FONT_STYLE, 13))
            lbl.pack()
            lbl.place(x=lx[i], y=ly[i])
            entry = Entry(widget_frame, bg=COLORS["BLUE"], fg=COLORS["WHITE"])
            entry.pack()
            entry.place(x=ex[i], y=ey[i])
            entry.insert(0, txt[i])
            entry.bind("<Button-1>", lambda event, ent=entry: clear(event, ent))
            self.entries.append(entry)

        self.sid = StringVar()
        self.start = StringVar()
        self.end = StringVar()
        self.pressure = StringVar()

        self.sid.set("1")
        self.start.set(str(datetime.today().date().strftime("%Y:%m:%d")) + " " + "00:00:00")
        self.end.set(str(datetime.today().date().strftime("%Y:%m:%d")) + " " + "23:59:59")
        self.pressure.set("50")

        self.entries[2]["textvariable"] = self.sid
        self.entries[4]["textvariable"] = self.start
        self.entries[5]["textvariable"] = self.end
        self.entries[8]["textvariable"] = self.pressure

        txt = ["<<<", "update", "plot", "read"]
        x, y = [0, 825, 825, 825], [0, 17, 57, 97]
        self.buttons = []

        for i in range(len(txt)):
            btn = Button(widget_frame, text=txt[i], bg=COLORS["LIGHT_GREEN"], fg=COLORS["WHITE"], width=7)
            btn.pack()
            btn.place(x=x[i], y=y[i])
            self.buttons.append(btn)

        self.in_pressure = StringVar()
        self.out_pressure = StringVar()

        variables = [self.in_pressure, self.out_pressure]
        txts = ["Station In Pressure", "Station Out Pressure"]
        lblx , lbly = [400, 700], [125, 125]

        for i in range(len(variables)):
            lb = Label(widget_frame, text=txts[i], bg=COLORS["BLUE_HEX"])
            lb.pack()
            lb.place(x=lblx[i] - 150, y=lbly[i])

            lbl = Label(widget_frame, textvariable=variables[i], bg=COLORS["BLUE_HEX"])
            lbl.pack()
            lbl.place(x=lblx[i], y=lbly[i])

    def destroy(self):
        self.frame.destroy()
