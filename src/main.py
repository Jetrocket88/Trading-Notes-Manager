# src/main.py
from tkinter import ttk

import tradeEntryWindow
import viewAllTradesWindow

import database
import globals
import styles
import tinker
import helpers

import ctypes
import sys


if __name__ == "__main__":
    if sys.platform == "win32":
        ctypes.windll.shcore.SetProcessDpiAwareness(1)


    w, h = helpers.screenRes() 
    root = tinker.initWindow(globals.WIDTH, globals.HEIGHT, (w// 2 - globals.WIDTH // 2, h // 2 - globals.HEIGHT // 2))

    #TODO add custom bar to make UX better
    #root.overrideredirect(True)


    styles.initStyle(root)


    container = ttk.Frame(root,  padding=20)
    container.pack(fill="both", expand=True)
    container.columnconfigure((0, 1, 2), weight=1)

    database.initDb()


    titleLabel = tinker.makeStaticLabel(root=root, container=container, text="Trading Notes", fontSize=30)
    titleLabel.grid(row = 0, column = 0, pady=(0, 10), sticky="ew", columnspan=3)
    titleLabel.configure(anchor="center")


    currentTimeVar = tinker.makeTextVar(database.getNow())
    timeLabel = tinker.makeDynamicLabel(root=root, container=container, textVar=currentTimeVar)
    timeLabel.grid(row = 1, column = 0, pady=(0, 10), sticky="ew", columnspan=3)
    timeLabel.configure(anchor="center")


    tinker.makeButton(container=container, text="Add a Trade", command=lambda: tradeEntryWindow.initTradeWindow(root)).grid(row=2, column=0, sticky="e")
    tinker.makeButton(container=container, text="View All Trades", command=lambda: viewAllTradesWindow.initViewWindow(root)).grid(row=2, column=1)
    tinker.makeButton(container=container, text="IDK", command=lambda: exit()).grid(row=2, column=2, sticky="w")

    tinker.updateTime(root, currentTimeVar)
    root.mainloop()

