from tkinter import *
from tkinter.ttk import Progressbar
from Projects.SNGPL.Requirements import COLORS, TITLE, FONT_STYLE
from Projects.SNGPL.utilities import start_bar


class LoadingScreen:
    def __init__(self, root, imgs=None, frame=None) -> None:
        if frame is not None:
            frame.destroy()
        self.frame = Frame(root, bg=COLORS["BLUE_HEX"])
        self.frame.pack(fill=BOTH, expand=True)

        self.complete = False

        title = Label(self.frame, text=TITLE, font=(FONT_STYLE, 20), bg=COLORS["BLUE_HEX"], fg=COLORS["DARK_BLUE"])
        title.pack()
        title.place(x=100, y=100)

        progress_bar = Progressbar(self.frame, orient=HORIZONTAL, length=500)
        progress_bar.pack()
        progress_bar.place(x=200, y=450)

        percents = StringVar()
        tasks = StringVar()
        variables = [percents, tasks]
        x, y = [435, 330], [475, 515]
        for i in range(len(variables)):
            label = Label(self.frame, bg=COLORS["BLUE_HEX"], fg=COLORS["DARK_BLUE"], textvariable=variables[i], font=FONT_STYLE)
            label.pack()
            label.place(x=x[i], y=y[i])

        img = [imgs[0], imgs[3]]
        x, y = [800, 325], [80, 175]
        for i in range(len(img)):
            image = Label(self.frame, image=img[i], bg=COLORS["BLUE_HEX"])
            image.pack()
            image.place(x=x[i], y=y[i])

        self.complete = start_bar(root, progress_bar, percents, tasks)

    def destroy(self):
        self.frame.destroy()
