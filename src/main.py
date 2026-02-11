# src/main.py
import tinker as tk
import database as db
import ctypes
import sys

WIDTH = 800
HEIGHT = 600
CENTER = (WIDTH / 2, HEIGHT / 2)

def exit(connection, root):
    connection.close()
    root.destroy()


def addATrade():
    pass


def centerOffset(x, y):
    return (CENTER[0] + x, CENTER[1] + y)

def topOffset(y):
    return -HEIGHT/2 + y


"""
adding an y position makes it go down
adding an x position makes it go right
"""

if __name__ == "__main__":
    if sys.platform == "win32":
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

    root = tk.initWindow(WIDTH, HEIGHT)

    db.initDb()
    button = tk.makeButton(root, "Add a trade", lambda: exit(db.connect(), root), centerOffset(0, topOffset(80)), None, None)

    currentTimeVar = tk.makeTextVar(db.getNow())
    timeLabel = tk.makeDynamicLabel(root, currentTimeVar, centerOffset(0, topOffset(30)), None, None)

    tk.updateTime(root, currentTimeVar)
    root.mainloop()
