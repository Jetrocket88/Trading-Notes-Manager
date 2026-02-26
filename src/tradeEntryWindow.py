import tinker
import inputs
import database

from tkinter import messagebox
import tkinter as tk


#DEBUGGING 
def fillWithDummyData(inputDict):
    inputDict["entryDate"].insert(0, "2009-9-9")
    inputDict["exitDate"].insert(0, "2009-9-9")
    inputDict["marketStructure"].insert("1.0", "well structured")
    inputDict["type"].insert(0, "Swing")
    inputDict["bias"].insert("1.0", "very biased")
    inputDict["risk"].insert(0, "4")
    inputDict["result"].insert(0, "Win")
    inputDict["emotions"].insert("1.0", "Very angery")
    inputDict["takeaways"].insert("1.0", "chinese mate")
    inputDict["accountType"].insert(0, "Live")
    inputDict["rewardRatio"].insert(0, "8")
    inputDict["symbol"].insert(0, "DXY")




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
    popup.destroy()



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


    #symbol
    inputs.addLabel(popup, container, "Symbol",  row=22)
    inputs.addHelp(popup, container, "Example: DXY, GBG/USD\nCan be in any format you like", row=23)
    inputs.addInput(container, inputDict, "symbol", row=23)


    submitButton = inputs.addButton(container, "Submit", lambda: handleSubmitData(popup, inputDict), row=24)
    submitButton.grid(columnspan=3, column=0, sticky="ew", pady=(30, 10))

    inputs.addButton(container, "DEBUG: FILL WITH DATA", lambda: fillWithDummyData(inputDict), row=25)

    return popup


