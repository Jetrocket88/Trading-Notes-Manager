import tinker
import inputs
import database

from tkinter import messagebox
import tkinter as tk


def clearSelection(event):
    event.widget.selection_clear()

def addTodaysDateToWidget(widget, text, position="end"):
    widget.delete(0, tk.END)
    widget.insert(position, text)



def handleSubmitData(popup, inputDict):
    data = {}
    errors = []

    for key, value in inputDict.items():
        result = inputs.getDataFromWidget(value)
        if result is None or str(result).strip() == "":
            errors.append(f"{key} cannot be empty")
        else:
            data[key] = result

    if errors:
        messagebox.showerror("Validation Error", "\n".join(errors))
        return None
    
    database.insertToDb(data)
    popup.close()



def initTradeWindow(root):
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
    inputs.addTextarea(container, inputDict, "takeaways", row=17, height=3)

    #accountType
    inputs.addLabel(popup, container, "Account Type", row=18)
    options = ("Live", "Paper", "Eval")
    inputs.addCombo(container, options, inputDict, "accountType", row=19, function=clearSelection)

    #rewardRatio
    inputs.addLabel(popup, container, "Reward Ratio", row=20)
    inputs.addHelp(popup, container, "1 : ? RR", row=21, column=2)

    inputs.addInput(container, inputDict, "rewardRatio", row=21)


    inputs.addLabel(popup, container, "Pair",  row=22)
    inputs.addHelp(popup, container, "Example: DXY, GBG/USD\nCan be in any format you like", row=23)
    inputs.addInput(container, inputDict,  "pair", row=23)


    submitButton = inputs.addButton(container, "Submit", lambda: handleSubmitData(popup, inputDict), row=24)
    submitButton.grid(columnspan=3, column=0, sticky="ew", pady=(30, 10))

    return popup


