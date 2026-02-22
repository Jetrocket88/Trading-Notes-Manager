# src/main.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import database
import globals
import styles
import tinker
import helpers
import inputs

import ctypes
import sys


def clearSelection(event):
    event.widget.selection_clear()

def addTodaysDateToWidget(widget, text, position="end"):
    widget.delete(0, tk.END)
    widget.insert(position, text)


def getDataFromWidget(widget):
    if isinstance(widget, tk.Text):
        return widget.get("1.0", "end-1c") 
    else:
        return widget.get()

def getInputValues(inputDict):
    values = [
        widget.get("1.0", "end-1c") if isinstance(widget, tk.Text)
        else widget.get()
        for widget in inputDict.values()
    ]   
    return values


def handleSubmitData(inputDict):
    data = {}
    errors = []

    for key, value in inputDict.items():
        result = getDataFromWidget(value)
        if result is None or str(result).strip() == "":
            errors.append(f"{key} cannot be empty")
        else:
            data[key] = result

    if errors:
        messagebox.showerror("Validation Error", "\n".join(errors))
        return None
    
    database.insertToDb(data)



def manageTradeEntryWindow(root):
    #window stuff
    width = 800
    height = 800
    popup = tinker.openPopup(root, "Trade Info", (width, height))

    #container
    container = tinker.makeScrollableFrame(popup, padding=0)

    container.columnconfigure(0, weight=1)
    container.rowconfigure(0, weight=0)

    inputDict = {}

    #date
    inputs.addLabel(popup, container, "Entry Date", row=0)
    entryDateInput = inputs.addInput(container, inputDict, "entryDate", row=1)
    inputs.addButton(container, "Open Calendar", lambda: tinker.openCalendarPopup(popup,entryDateInput), row=1)
    inputs.addHelp(popup, container, "Should be in format\n(xx/xx/xx/xxxx)",row=1)

    inputs.addLabel(popup, container, "Exit Date", row=2)
    exitDateInput = inputs.addInput(container, inputDict, "exitDate", row=3)
    inputs.addButton(container, "Open Calendar", lambda: tinker.openCalendarPopup(popup, exitDateInput), row=3)






    marketStrucutreText = "Talk about why you took the trade and confluences that made you certain in the direction of price"
    inputs.addLabel(popup, container, "Market Structure", row=4)
    inputs.addHelp(popup, container, marketStrucutreText, row=5, column=2, sticky="ns")
    inputs.addTextarea(container, inputDict, "marketStructure", row=5, height=4)

    #type of trade
    inputs.addLabel(popup, container, text="Type of Trade", row=6)
    options = ("Swing", "Inter-Day")
    inputs.addCombo(container,options, inputDict, "type", row=7, function=clearSelection)

    #Bias
    inputs.addLabel(popup, container, "Bias", row=8)

    biasGuide = "Did the trade align with your weekly bias? Or the daily one?"
    inputs.addHelp(popup, container, biasGuide, row=9, column=2)
    inputs.addTextarea(container, inputDict, "bias", row=9, height=3)

    #risk
    inputs.addLabel(popup, container, "Risk", row=10)
    riskGuide = "% of account size risked?"
    inputs.addHelp(popup, container, riskGuide, row=11, column=2)
    inputs.addInput(container, inputDict, "risk", row=11)

    #result
    inputs.addLabel(popup, container, "Result", row=12)
    options = ("Win", "Loss", "BE")
    inputs.addCombo(container, options, inputDict, "result", row=13, function=clearSelection)


    #Emotions
    emotionGuide = "How did you feel? FOMO?\nOvertrading?"
    inputs.addLabel(popup, container, "Emotions", row=14)
    inputs.addHelp(popup, container, emotionGuide, row=15, column=2)
    inputs.addTextarea(container, inputDict, "emotions", row=15, height=3)

    #Takeaways
    takeawayGuide = "What worked? What didn't?"
    inputs.addLabel(popup, container, "Takeaways", row=16)
    inputs.addHelp(popup, container, takeawayGuide, row=17, column=2)
    inputs.addTextarea(container, inputDict, "takeaway", row=17, height=3)

    #accountType
    inputs.addLabel(popup, container, "Account Type", row=18)
    options = ("Live", "Paper", "Eval")
    inputs.addCombo(container, options, inputDict, "accountType", row=19, function=clearSelection)

    #rewardRatio
    inputs.addLabel(popup, container, "Reward Ratio", row=20)
    inputs.addHelp(popup, container, "1 : ? RR", row=21, column=2)

    inputs.addInput(container, inputDict, "rewardRatio", row=21)

    submitButton = inputs.addButton(container, "Submit", lambda: handleSubmitData(inputDict), row=22)
    submitButton.grid(columnspan=3, column=0, sticky="ew")






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
    titleLabel.grid(row = 0, column = 0, pady=(0, 10), sticky="ew")
    titleLabel.configure(anchor="center")

    #clock
    currentTimeVar = tinker.makeTextVar(database.getNow())
    timeLabel = tinker.makeDynamicLabel(root=root, container=container, textVar=currentTimeVar)
    timeLabel.grid(row = 1, column = 0, pady=(0, 20), sticky="ew")
    timeLabel.configure(anchor="center")

    #add trade button
    button = tinker.makeButton(container=container, text="Add a trade", command=lambda: manageTradeEntryWindow(root))
    button.grid(row=2, column=0)


    #mainloop
    tinker.updateTime(root, currentTimeVar)
    root.mainloop()

