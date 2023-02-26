from tkinter import *
from PIL import Image, ImageTk
from Projects.SNGPL.Requirements import *
from Projects.SNGPL.MainScreen import MainScreen
from Projects.SNGPL.ScreenManager import open_login
from Projects.SNGPL.LoadingScreen import LoadingScreen
from Projects.SNGPL.LoginScreen import LoginScreen
from Projects.SNGPL.RegisterScreen import RegisterScreen
from Projects.SNGPL.SiteScreen import SiteScreen
from Projects.SNGPL.utilities import destroy


root = Tk()

imgs = []
for i in range(len(images)):
    imgs.append(PhotoImage(file=images[i]))

icon = ImageTk.PhotoImage(Image.open("../imgs/new-sngpl.png"))

root.title(TITLE)
root.iconphoto(root, icon)
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(width=False, height=False)
root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)
root.config(bg=COLORS["BLUE_HEX"])
root.bind("<Alt-F4>", lambda event, r=root: destroy(event, r))
root.focus_force()
root.state("zoomed")

# screen = LoadingScreen(root, imgs=imgs)
# screen = MainScreen(root, imgs=imgs)
# screen = LoginScreen(root, imgs=imgs)
screen = RegisterScreen(root, imgs=imgs)
# screen = SiteScreen(root, imgs=imgs)

root.mainloop()
