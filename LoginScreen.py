from tkinter import *
from Projects.SNGPL.utilities import clear
from Projects.SNGPL.Requirements import COLORS, FONT_STYLE, SIZES, BOLD
from Projects.SNGPL.AutoComplete import AutocompleteEntry
from Projects.SNGPL.Requirements import username_admin, username_operator, username_calibrator


class LoginScreen:
    def __init__(self, root, frame=None, user=None, imgs=None) -> None:
        if frame is not None:
            frame.destroy()
        self.frame = Frame(root, bg=COLORS["BLUE_HEX"])
        self.frame.pack(fill=BOTH, expand=True)

        user_list = [username_admin, username_operator, username_calibrator]
        txtlbl = ["<<<", "login", "email", "password", "email", "password", str(user.upper())]
        self.buttons = []
        self.entries = []
        for i in range(len(txtlbl)):
            if i <= 1:
                btn = Button(self.frame, text=txtlbl[i], bg=COLORS["LIGHT_GREEN"], fg=COLORS["WHITE"], width=20, height=2)
                btn.pack()
                btn.place(x=(400 * i) + 5, y=(400 * i) + 5)
                self.buttons.append(btn)
            elif 1 < i < 4:
                lbl = Label(self.frame, text=txtlbl[i], font=(FONT_STYLE, SIZES[15], BOLD), bg=COLORS["BLUE_HEX"],
                            fg=COLORS["DARK_BLUE"])
                lbl.pack()
                lbl.place(x=250, y=150 + (75 * (i - 1)))
            elif 3 < i < (len(txtlbl) - 1):
                if i == 4:
                    entry = AutocompleteEntry(self.frame, width=20, font=(FONT_STYLE, SIZES[15]), bg=COLORS["BLUE"], fg=COLORS["WHITE"])
                    entry.set_completion_list(user_list)
                    entry.insert(0, txtlbl[i])
                    entry.pack()
                    entry.place(x=400, y=150 + (75 * (i - 3)))
                    entry.bind("<Button-1>", lambda event, ent=entry: clear(event, ent))
                    self.entries.append(entry)
                if i == 5:
                    entry = Entry(self.frame, width=20, font=(FONT_STYLE, SIZES[15]), bg=COLORS["BLUE"], fg=COLORS["WHITE"], show="*")
                    entry.insert(0, txtlbl[i])
                    entry.pack()
                    entry.place(x=400, y=150 + (75 * (i - 3)))
                    entry.bind("<Button-1>", lambda event, ent=entry: clear(event, ent))
                    self.entries.append(entry)
            else:
                lbl = Label(self.frame, text=txtlbl[len(txtlbl) - 1], font=(FONT_STYLE, SIZES[15]),
                            bg=COLORS["BLUE_HEX"], fg=COLORS["DARK_BLUE"])
                lbl.pack()
                lbl.place(x=360, y=160)

        img = [imgs[0], imgs[1], imgs[2]]
        x, y = [415, 368, 368], [50, 225, 300]

        for i in range(len(img)):
            lb = Label(self.frame, image=img[i], bg=COLORS["BLUE_HEX"])
            lb.pack()
            lb.place(x=x[i], y=y[i])

    def destroy(self):
        self.frame.destroy()
