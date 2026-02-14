# src/main.py
import tkinter as tk
from tkinter import ttk

import database
import globals
import styles
import tinker
import helpers
import inputs


import ctypes
import sys

def addTodaysDateToWidget(widget, text, position="end"):
    widget.delete(0, tk.END)
    widget.insert(position, text)


def manageTradeEntryWindow(root):
    #window stuff
    width = 800
    height = 800
    popup = tinker.openPopup(root, "Trade Info", (width, height))

    #container
    container, update_scroll = tinker.makeScrollableFrame(popup, padding=0)

    container.columnconfigure(0, weight=1)
    container.rowconfigure(0, weight=0)

    inputDict = {}

    #date inputs
    #entry date
    entryDateLabel = tinker.makeStaticLabel(popup, container, "Entry Date")
    entryDateLabel.grid(row=0, column=0, pady=(0, 10), sticky="ew")

    entryDateInput = inputs.makeInput(container, inputDict, "entryDate", multiline=False, height=10)
    entryDateInput.grid(row=1, column=0, pady=(0, 10), sticky="ew")

    entryDateButton = tinker.makeButton(container, "Use Today's Date", lambda: addTodaysDateToWidget(entryDateInput, database.getNow()))
    entryDateButton.grid(row=1, column=2, pady=(0, 10))

    entryDateGuide = tinker.makeStaticLabel(popup, container, "Should be in format\n(xx/xx/xx/xxxx)", fontSize=7)
    entryDateGuide.configure(foreground="gray38")
    entryDateGuide.grid(row=1, column=1, pady=(0,10), padx=(10, 40), sticky="ew")

    #exit date 
    exitDateLabel = tinker.makeStaticLabel(popup, container, "Exit Date")
    exitDateLabel.grid(row=2, column=0, pady=(0, 10), sticky="ew")

    exitDateInput = inputs.makeInput(container, inputDict, "exitDate", multiline=False, height=10)
    exitDateInput.grid(row=3, column=0, pady=(0, 10), sticky="ew")

    exitDateButton = tinker.makeButton(container, "Use Today's Date", lambda: addTodaysDateToWidget(exitDateInput, database.getNow()))
    exitDateButton.grid(row=3, column=2, pady=(0, 10))

    #market structure
    marketStructureLabel = tinker.makeStaticLabel(popup, container, "Market structure")
    marketStructureLabel.grid(row=4, column=0, pady=(0, 0), sticky="ew")

    marketStructureGuide = "Should talk about why you took the trade and the confluences that made you certain in the direction of price"
    marketStructureGuideLabel = tinker.makeStaticLabel(popup, container, marketStructureGuide, fontSize=7)
    marketStructureGuideLabel.configure(foreground="gray38", wraplength=300)
    marketStructureGuideLabel.grid(row=4, column=1, pady=(0, 0), padx=(10, 10), sticky="e", columnspan=1)

    marketStructureFont = styles.getDefaultFont()
    marketStructureFont.configure(size=9)
    marketStructureTextArea = inputs.makeInput(container, inputDict, "marketStructure", width=60, height=4, multiline=True, font=marketStructureFont)
    marketStructureTextArea.grid(row=5, column=0, pady=(10, 0), sticky="e", columnspan=2)


    #type of trade
    typeLabel = tinker.makeStaticLabel(popup, container, "Type of trade")
    typeLabel.grid(row=6, column=0, pady=(10, 0), padx=(0, 0), sticky="w", columnspan=1)

    options = ("Swing", "Inter-Day")
    typeBox = inputs.makeComboBox(container, options)
    typeBox.grid(row=7, column=0, pady=(10,0), padx=(0, 0), sticky="w")
    


    # Test element at bottom
    testLabel = tinker.makeStaticLabel(popup, container, "BOTTOM TEST ELEMENT", fontSize=30)
    testLabel.configure(foreground="red")
    testLabel.grid(row=100, column=0, pady=(2000, 50), sticky="w")  # Even more padding
    
    
    # Multiple update attempts
    popup.after(100, update_scroll)
    popup.after(500, update_scroll)
    

    return popup
    



if __name__ == "__main__":
    if sys.platform == "win32":
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

    #initialise window
    w, h = helpers.screenRes() 
    root = tinker.initWindow(globals.WIDTH, globals.HEIGHT, (w// 2 - globals.WIDTH // 2, h // 2 - globals.HEIGHT // 2))

    #initialise style
    styles.initStyle(root)

    #initialise container
    container = ttk.Frame(root,  padding=20)
    container.pack(fill="both", expand=True)
    container.columnconfigure(0, weight=1)

    database.initDb()

    #title label
    titleLabel = tinker.makeStaticLabel(root=root, container=container, text="Trading Notes", fontSize=30)
    titleLabel.grid(row = 0, column = 0, pady=(0, 10))

    #clock
    currentTimeVar = tinker.makeTextVar(database.getNow())
    timeLabel = tinker.makeDynamicLabel(root=root, container=container, textVar=currentTimeVar)
    timeLabel.grid(row = 1, column = 0, pady=(0, 20))

    #add trade button
    button = tinker.makeButton(container=container, text="Add a trade", command=lambda: manageTradeEntryWindow(root))
    button.grid(row=2, column=0)


    #mainloop
    root.mainloop()
    tinker.updateTime(root, currentTimeVar)
