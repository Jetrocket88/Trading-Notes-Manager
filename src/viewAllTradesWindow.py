import tinker
import inputs
import database

import tkinter as tk

#initial ideas
#Pair, profit / loss, entryDate, long / short
# ------------------------
# | AAPL      +£120     |
# | 12/02/26  Long      |
# ------------------------

class TradeCard(tk.Frame):
    def __init__(self, parent, tradeData, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.tradeData = tradeData
        #self.configure(relief="ridge", bg=2, padx=10, pady=10)
        
        #symbolLabel = inputs.addLabel(self, self, tradeData.symbol)


def initViewWindow(root):
    #window stuff
    width = 800
    height = 800
    popup = tinker.openPopup(root, "Trade Info", (width, height))

    #container
    container = tinker.makeScrollableFrame(popup, padding=0)

    container.columnconfigure(0, weight=1)
    container.rowconfigure(0, weight=0)

    titleLabel = tinker.makeStaticLabel(popup, container, "All Logged Trades", fontSize=20)
    titleLabel.grid(row=0, column=0)
    titleLabel.configure(anchor="center")

    #Get all data to display
    rows = database.executeSelectQuery("SELECT * FROM Trades")
    trades = database.readIntoClasses(rows)
    for trade in trades:
        pass








