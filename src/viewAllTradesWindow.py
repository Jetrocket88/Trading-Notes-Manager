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
        self.configure(relief="ridge", bd=2, padx=10, pady=10)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)


        inputs.addLabel(self, self, tradeData.symbol, row=1)

        


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
    card = TradeCard(container, trades[0])
    card.grid(row=1, column=0)








