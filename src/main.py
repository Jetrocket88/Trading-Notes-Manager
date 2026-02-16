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


def clearSelection(event):
    event.widget.selection_clear()

def addTodaysDateToWidget(widget, text, position="end"):
    widget.delete(0, tk.END)
    widget.insert(position, text)


def getInputValues(inputDict):
    values = [
        widget.get("1.0", "end-1c") if isinstance(widget, tk.Text)
        else widget.get()
        for widget in inputDict.values()
    ]   
    return values



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
    leftPad = 10

    wrap = 200
    #date inputs
    #entry date
    entryDateLabel = tinker.makeStaticLabel(popup, container, "Entry Date")
    entryDateLabel.grid(row=0, column=0, pady=(20, 10), sticky="ew", padx=(leftPad, 0))

    entryDateInput = inputs.makeInput(container, inputDict, "entryDate", multiline=False, height=10)
    entryDateInput.grid(row=1, column=0, pady=(0, 10), sticky="ew", padx=(leftPad, 0))

    entryDateButton = tinker.makeButton(container, "Use Today's Date", lambda: addTodaysDateToWidget(entryDateInput, database.getNow()))
    entryDateButton.grid(row=1, column=2, pady=(0, 10))

    entryDateGuide = tinker.makeStaticLabel(popup, container, "Should be in format\n(xx/xx/xx/xxxx)", fontSize=7)
    entryDateGuide.configure(foreground="gray38")
    entryDateGuide.grid(row=1, column=1, pady=(0,10), padx=(10, 40), sticky="ws")

    #exit date 
    exitDateLabel = tinker.makeStaticLabel(popup, container, "Exit Date")
    exitDateLabel.grid(row=2, column=0, pady=(0, 10), sticky="ew", padx=(leftPad, 0))

    exitDateInput = inputs.makeInput(container, inputDict, "exitDate", multiline=False, height=10)
    exitDateInput.grid(row=3, column=0, pady=(0, 10), sticky="ew", padx=(leftPad, 0))

    exitDateButton = tinker.makeButton(container, "Use Today's Date", lambda: addTodaysDateToWidget(exitDateInput, database.getNow()))
    exitDateButton.grid(row=3, column=2, pady=(0, 10))

    #market structure
    marketStructureLabel = tinker.makeStaticLabel(popup, container, "Market structure")
    marketStructureLabel.grid(row=4, column=0, pady=(0, 0), sticky="ew", padx=(leftPad, 0))

    marketStructureGuide = "Talk about why you took the trade and confluences that made you certain in the direction of price"
    marketStructureGuideLabel = tinker.makeStaticLabel(popup, container, marketStructureGuide, fontSize=7)
    marketStructureGuideLabel.configure(foreground="gray38", wraplength=wrap)
    marketStructureGuideLabel.grid(row=4, column=1, pady=(0, 0), padx=(10, 10), sticky="ws", columnspan=1)

    marketStructureFont = styles.getDefaultFont()
    marketStructureFont.configure(size=9)
    marketStructureTextArea = inputs.makeInput(container, inputDict, "marketStructure", width=60, height=2, multiline=True, font=marketStructureFont)
    marketStructureTextArea.grid(row=5, column=0, pady=(10, 0), sticky="ew", columnspan=2, padx=(leftPad, 0))


    #type of trade
    typeLabel = tinker.makeStaticLabel(popup, container, "Type of trade")
    typeLabel.grid(row=6, column=0, pady=(10, 0), padx=(leftPad, 0), sticky="w", columnspan=1)

    options = ("Swing", "Inter-Day")
    typeBox = inputs.makeComboBox(container, options)
    typeBox.grid(row=7, column=0, pady=(10,0), padx=(leftPad, 0), sticky="w")
    typeBox.bind("<Button-1>", clearSelection)
    typeBox.bind("<FocusIn>", clearSelection)
    inputDict["type"] = typeBox


    #Bias
    biasLabel= tinker.makeStaticLabel(popup, container, "Bias")
    biasLabel.grid(row=8, column=0, pady=(20, 0), sticky="ew", padx=(leftPad, 0))

    biasGuide = "Did the trade align with your weekly bias? Or the daily one?"
    biasGuideLabel = tinker.makeStaticLabel(popup, container, biasGuide, fontSize=7)
    biasGuideLabel.configure(foreground="gray38", wraplength=wrap)
    biasGuideLabel.grid(row=8, column=1, pady=(0, 0), padx=(10, 10), sticky="ws", columnspan=1)

    biasFont = styles.getDefaultFont()
    biasFont.configure(size=9)
    biasTextArea = inputs.makeInput(container, inputDict, "bias", width=60, height=2, multiline=True, font=biasFont)
    biasTextArea.grid(row=9, column=0, pady=(10, 0), sticky="ew", columnspan=2, padx=(leftPad, 0))


    #risk
    riskLabel = tinker.makeStaticLabel(popup, container, "Risk", width=10)
    riskLabel.grid(row=10, column=0, pady=(20, 10), sticky="ew", padx=(leftPad, 0))

    riskGuide = "% of account size risked?"
    riskGuideLabel = tinker.makeStaticLabel(popup, container, riskGuide, fontSize=7)
    riskGuideLabel.configure(foreground="gray38", wraplength=wrap)
    riskGuideLabel.grid(row=11, column=1, pady=(00, 10), padx=(10, 10), sticky="ns", columnspan=1)

    riskInput = inputs.makeInput(container, inputDict, "risk", multiline=False, height=10)
    riskInput.grid(row=11, column=0, pady=(0, 10), sticky="ew", padx=(leftPad, 0))
    inputDict["risk"] = riskInput

    #result
    resultLabel = tinker.makeStaticLabel(popup, container, "Result")
    resultLabel.grid(row=12, column=0, pady=(10, 0), padx=(leftPad, 0), sticky="w", columnspan=1)

    options = ("Win", "Loss", "BE")
    resultBox = inputs.makeComboBox(container, options)
    resultBox.grid(row=13, column=0, pady=(10,0), padx=(leftPad, 0), sticky="w")
    resultBox.bind("<Button-1>", clearSelection)
    resultBox.bind("<FocusIn>", clearSelection)
    inputDict["result"] = resultBox


    #Emotions
    emotionLabel= tinker.makeStaticLabel(popup, container, "Emotions")
    emotionLabel.grid(row=14, column=0, pady=(20, 0), sticky="ew", padx=(leftPad, 0))

    emotionGuide = "How did you feel? FOMO?\nOvertrading?"
    emotionGuideLabel = tinker.makeStaticLabel(popup, container, emotionGuide, fontSize=7)
    emotionGuideLabel.configure(foreground="gray38", wraplength=wrap)
    emotionGuideLabel.grid(row=14, column=1, pady=(0, 0), padx=(10, 10), sticky="ws", columnspan=1)

    emotionFont = styles.getDefaultFont()
    emotionFont.configure(size=9)
    emotionTextArea = inputs.makeInput(container, inputDict, "emotion", width=60, height=2, multiline=True, font=emotionFont)
    emotionTextArea.grid(row=15, column=0, pady=(10, 0), sticky="ew", columnspan=2, padx=(leftPad, 0))


    #Takeaways
    takeawayLabel = tinker.makeStaticLabel(popup, container, "Takeaways")
    takeawayLabel.grid(row=16, column=0, pady=(20, 0), sticky="ew", padx=(leftPad, 0))

    takeawayGuide = "What worked? What didn't?"
    takeawayGuideLabel = tinker.makeStaticLabel(popup, container, takeawayGuide, fontSize=7)
    takeawayGuideLabel.configure(foreground="gray38", wraplength=wrap)
    takeawayGuideLabel.grid(row=16, column=1, pady=(0, 0), padx=(10, 10), sticky="ws", columnspan=1)

    takeawayFont = styles.getDefaultFont()
    takeawayFont.configure(size=9)
    takeawayTextArea = inputs.makeInput(container, inputDict, "takeaway", width=60, height=2, multiline=True, font=takeawayFont)
    takeawayTextArea.grid(row=17, column=0, pady=(10, 0), sticky="ew", columnspan=2, padx=(leftPad, 0))

    #accountType
    accountTypeLabel = tinker.makeStaticLabel(popup, container, "Account Type")
    accountTypeLabel.grid(row=18, column=0, pady=(10, 0), padx=(leftPad, 0), sticky="w", columnspan=1)

    options = ("Live", "Paper", "Eval")
    accountTypeBox = inputs.makeComboBox(container, options)
    accountTypeBox.grid(row=19, column=0, pady=(10,0), padx=(leftPad, 0), sticky="w")
    accountTypeBox.bind("<Button-1>", clearSelection)
    accountTypeBox.bind("<FocusIn>", clearSelection)
    inputDict["accountType"] = accountTypeBox

    #rewardRatio
    rewardRatioLabel = tinker.makeStaticLabel(popup, container, "Reward Ratio", width=10)
    rewardRatioLabel.grid(row=20, column=0, pady=(20, 10), sticky="ew", padx=(leftPad, 0))

    rewardRatioGuide = "1 : ? RR"
    rewardRatioGuideLabel = tinker.makeStaticLabel(popup, container, rewardRatioGuide, fontSize=7)
    rewardRatioGuideLabel.configure(foreground="gray38", wraplength=wrap)
    rewardRatioGuideLabel.grid(row=21, column=1, pady=(0, 10), padx=(10, 10), sticky="n", columnspan=1)

    rewardRatioInput = inputs.makeInput(container, inputDict, "rewardRatio", multiline=False, height=10)
    rewardRatioInput.grid(row=21, column=0, pady=(0, 10), sticky="ew", padx=(leftPad, 0))
    inputDict["rewardRatio"] = rewardRatioInput 

    submitButton = tinker.makeButton(container, "Submit", lambda: database.insertToDb(getInputValues(inputDict)))
    submitButton.grid(row=22, column=0, pady=(10, 10), padx=(10, 10), columnspan=3, sticky="we")
    
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
    root.mainloop()
    tinker.updateTime(root, currentTimeVar)
