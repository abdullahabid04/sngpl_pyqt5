from tkinter import *
from Projects.SNGPL.Requirements import COLORS, FONT_STYLE
from Projects.SNGPL.utilities import clear


class RegisterScreen:
    def __init__(self, root, frame=None, imgs=None) -> None:
        if frame is not None:
            frame.destroy()
        self.frame = Frame(root, bg=COLORS["BLUE_HEX"])
        self.frame.pack(fill=BOTH, expand=True)

        img = Label(self.frame, image=imgs[0], bg=COLORS["BLUE_HEX"])
        img.pack()
        img.place(x=415, y=25)

        regframe = Frame(self.frame, width=600, height=400, bg=COLORS["HEX_BLUE"])
        regframe.pack(fill=BOTH, expand=True)
        regframe.place(x=150, y=100)

        usrframe = LabelFrame(regframe, width=600, height=40, bg=COLORS["BLUE_HEX"])
        usrframe.pack(fill=BOTH, expand=True)
        usrframe.place(x=0, y=350)

        regaslbl = Label(usrframe, text="Register As", font=(FONT_STYLE, 13), bg=COLORS["BLUE_HEX"], fg=COLORS["HEX_BLUE"])
        regaslbl.pack()
        regaslbl.place(x=50, y=5)

        values = [("Admin", "A"), ("Operator", "O"), ("Calibrator", "C")]
        rx, ry = [200, 300, 400], [5, 5, 5]
        i = 0

        self.option = StringVar()
        self.option.set("A")

        for text, value in values:
            rb = Radiobutton(usrframe, text=text, variable=self.option, value=value, bg=COLORS["BLUE_HEX"], activebackground=COLORS["BLUE_HEX"])
            rb.pack()
            rb.place(x=rx[i], y=ry[i])

            i += 1

        title = Label(regframe, text="Register Yourself", font=(FONT_STYLE, 15), bg=COLORS["HEX_BLUE"], fg=COLORS["BLUE_HEX"])
        title.pack()
        title.place(x=215, y=25)

        entxts = ["first name", "last name", "email", "password", "confirm password"]
        self.btns = []
        self.ents = []

        lblx , lbly = [100, 100, 100, 100, 100], [100, 150, 200, 250, 300]
        entx, enty = [250, 250, 250, 250, 250], [100, 150, 200, 250, 300]

        for i in range(len(entxts)):
            lbl = Label(regframe, text=entxts[i], font=(FONT_STYLE, 10), bg=COLORS["HEX_BLUE"],
                        fg=COLORS["DARK_BLUE"])
            lbl.pack()
            lbl.place(x=lblx[i], y=lbly[i])

            entry = Entry(regframe, width=20, font=(FONT_STYLE, 15), bg=COLORS["BLUE"], fg=COLORS["WHITE"])
            entry.insert(0, entxts[i])
            entry.pack()
            entry.place(x=entx[i], y=enty[i])
            entry.bind("<Button-1>", lambda event, ent=entry: clear(event, ent))
            self.ents.append(entry)

        txt = ["Register", "Login"]
        btnx, btny = [400, 400], [510, 540]

        for i in range(len(txt)):
            btn = Button(self.frame, text=txt[i], width=20, bg=COLORS["LIGHT_GREEN"], fg=COLORS["WHITE"])
            btn.pack()
            btn.place(x=btnx[i], y=btny[i])
            self.btns.append(btn)

    def destroy(self):
        self.frame.destroy()
