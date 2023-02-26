from tkinter import *
from Projects.SNGPL.Requirements import COLORS, FONT_STYLE, TITLE, LABEL_SELECT


class MainScreen:
    def __init__(self, root, frame=None, imgs=None) -> None:
        if frame is not None:
            frame.destroy()
        self.frame = Frame(root, bg=COLORS["BLUE_HEX"])
        self.frame.pack(fill=BOTH, expand=True)

        image = Label(self.frame, image=imgs[0], bg=COLORS["BLUE_HEX"])
        image.pack()
        image.place(x=800, y=80)

        x, y, txtlbl = [100, 250], [100, 250], [TITLE, LABEL_SELECT]

        for i in range(len(txtlbl)):
            lbl = Label(self.frame, text=txtlbl[i], font=(FONT_STYLE, 20 - (5 * i)), bg=COLORS["BLUE_HEX"],
                        fg=COLORS["DARK_BLUE"])
            lbl.pack()
            lbl.place(x=x[i], y=y[i])

        options = ["Administrator", "Operator", "Calibrator"]
        self.option = StringVar()
        self.option.set(options[0])
        drop_menu = OptionMenu(self.frame, self.option, *options)
        drop_menu.pack()
        drop_menu.place(x=600, y=250)

        btntxt = ["LOGIN", "REGISTER"]
        btnx, btny = [375, 375], [350, 400]
        self.btns = []

        for i in range(len(btntxt)):
            btn = Button(self.frame, text=btntxt[i], bg=COLORS["LIGHT_GREEN"], fg=COLORS["WHITE"], width=20, height=2)
            btn.pack()
            btn.place(x=btnx[i], y=btny[i])
            self.btns.append(btn)

    def destroy(self):
        self.frame.destroy()
