# src/main.py
import tinker as tk
import database as db
import ctypes
import sys

from helpers import WIDTH, HEIGHT
import helpers as h

def manageTradeEntryWindow(root):
    width = 800
    height = 800
    popup = tk.openPopup(root, "Trade Info", (width, height))

    leftPad = 20
    tk.makeStaticLabel(root=popup, text="Enter Trade Details", pos=(100, 100))

    inputs = {}
    tk.makeInput(popup, inputs, "entry date", pos=(leftPad, 80), dims=(30, 10), multiline=False)
    popup.mainloop()


"""
adding an y position makes it go down
adding an x position makes it go right
"""

if __name__ == "__main__":
    if sys.platform == "win32":
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

    width, height = h.screenRes() 
    #these width and height are the position of the window
    #on the screen, not the size of the window
    root = tk.initWindow(WIDTH, HEIGHT, (width // 2 - WIDTH // 2, height // 2 - HEIGHT // 2))

    db.initDb()
    titleLabel = tk.makeStaticLabel(root, "Trading Notes", h.centerOffset(0, h.topOffset(30, HEIGHT), WIDTH, HEIGHT), fontSize=30)

    currentTimeVar = tk.makeTextVar(db.getNow())
    timeLabel = tk.makeDynamicLabel(root, currentTimeVar, h.centerOffset(0, h.topOffset(80, HEIGHT), WIDTH, HEIGHT), None, None)

    button = tk.makeButton(root, "Add a trade", lambda: manageTradeEntryWindow(root), h.centerOffset(0, h.topOffset(140, HEIGHT), WIDTH, HEIGHT), None, None)

    tk.updateTime(root, currentTimeVar)



    root.mainloop()
