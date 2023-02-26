from tkinter import *
from PIL import Image, ImageTk
from Projects.SNGPL.Requirements import *
from Projects.SNGPL.MainScreen import MainScreen
from Projects.SNGPL.ScreenManager import open_login, open_register
from Projects.SNGPL.LoadingScreen import LoadingScreen
from Projects.SNGPL.utilities import destroy


def main():
    root = Tk()

    imgs = []
    for i in range(len(images)):
        imgs.append(PhotoImage(file=images[i]))

    icon = ImageTk.PhotoImage(Image.open("imgs/new-sngpl.png"))

    root.title(TITLE)
    root.iconphoto(root, icon)
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.resizable(width=False, height=False)
    root.minsize(WIDTH, HEIGHT)
    root.maxsize(WIDTH, HEIGHT)
    root.config(bg=COLORS["BLUE_HEX"])
    root.bind("<Alt-F4>", lambda event, r=root: destroy(event, r))
    root.focus_force()

    loading_screen = LoadingScreen(root, imgs=imgs)

    if loading_screen.complete is True:
        loading_screen.destroy()
        main_screen = MainScreen(root, imgs=imgs)
        user_main = main_screen.option
        btns_main = main_screen.btns
        cmds = [lambda u=user_main: open_login(root, main_screen.frame, u, imgs, main_screen.destroy()),
                lambda: open_register(root, main_screen.frame, imgs, main_screen.destroy())
                ]

        for i in range(len(cmds)):
            btns_main[i]["command"] = cmds[i]

    root.mainloop()


if __name__ == '__main__':
    main()
