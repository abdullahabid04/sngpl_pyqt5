from Projects.SNGPL.MainScreen import MainScreen
from Projects.SNGPL.LoginScreen import LoginScreen
from Projects.SNGPL.RegisterScreen import RegisterScreen
from Projects.SNGPL.backend import login


def open_main(root, screen, imgs, function):
    main_screen = MainScreen(root, frame=screen, imgs=imgs)
    user_main = main_screen.option
    btns_main = main_screen.btns
    cmds = [lambda u=user_main: open_login(root, main_screen.frame, u, imgs, main_screen.destroy()),
            lambda: open_register(root, main_screen.frame, imgs, main_screen.destroy())
            ]

    for i in range(len(cmds)):
        btns_main[i]["command"] = cmds[i]


def open_login(root, screen, user, imgs, function):
    login_screen = LoginScreen(root, frame=screen, user=user.get(), imgs=imgs)
    btn = login_screen.buttons
    entries = login_screen.entries
    cmds = [lambda r=root, s=login_screen.frame, im=imgs: open_main(r, s, im, login_screen.destroy()),
            lambda r=root, s=login_screen.frame, u=user, e=entries[0], p=entries[1]: login(r, s, u, e, p, imgs, open_main)]
    for i in range(len(cmds)):
        btn[i]["command"] = cmds[i]


def open_register(root, screen, imgs, function):
    register_screen = RegisterScreen(root, frame=screen, imgs=imgs)
    btns = register_screen.btns
    ents = register_screen.ents
    cmds = [lambda r=root, s=register_screen.frame, im=imgs: open_main(r, s, im, register_screen.destroy()),
            lambda r=root, s=register_screen.frame, im=imgs: open_main(r, s, im, register_screen.destroy())
            ]

    for i in range(len(cmds)):
        btns[i]["command"] = cmds[i]
