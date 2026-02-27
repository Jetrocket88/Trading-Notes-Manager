import tinker
import inputs
import database

import tkinter as tk
from tkinter import ttk

#initial ideas
#Pair, profit / loss, entryDate, long / short
# ------------------------
# | AAPL      +£120     |
# | 12/02/26  Long      |
# ------------------------

class TradeCard(ttk.Frame):
    def __init__(self, parent, tradeData, *args, **kwargs):
        super().__init__(parent, style="TradeCard.TFrame", *args, **kwargs)
        self.tradeData = tradeData
        self.configure(width=150, height=80)
        self.grid_propagate(False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        inputs.addLabel(self, self, tradeData.symbol, row=0, sticky="w")


def initViewWindow(root):
    #window stuff
    width = 800
    height = 800
    popup = tinker.openPopup(root, "All Trades", (width, height))

    popup.columnconfigure(0, weight=1)
    popup.rowconfigure(0, weight=1)

    #container
    container = tinker.makeScrollableFrame(popup, padding=0)
    container.grid(row=0, column=0, sticky="nsew")

    #configure container to expand row 1 (where the card container is )
    container.columnconfigure(0, weight=1)
    container.rowconfigure(1, weight=0)

    titleLabel = tinker.makeStaticLabel(popup, container, text="Logged Trades", fontSize=30)
    titleLabel.grid(row = 0, column = 0, pady=(0, 10), sticky="ew", columnspan=3)
    titleLabel.configure(anchor="center")

    #card container (should stretch whole regular container)
    cardContainer = ttk.Frame(container,  padding=20)
    cardContainer.grid(row=1, column=0, sticky="ew")
    cardContainer.configure(style="TESTING.TFrame")

    for col in range(3):
        cardContainer.columnconfigure(col, weight=1)


    #Get all data to display
    rows = database.executeSelectQuery("SELECT * FROM Trades")
    trades = database.readIntoClasses(rows)
    for trade in trades:
        pass
    

    numCards = len(trades)
    numCols = 3
    numRows = (numCards + numCols - 1) // numCols
    for row in range(numRows):
        cardContainer.rowconfigure(row, weight=0)

    #horizontal dummy data
    card = TradeCard(cardContainer, trades[0])
    card.grid(row=0, column=0, sticky="ew", padx=2, pady=5)

    card = TradeCard(cardContainer, trades[0])
    card.grid(row=0, column=1, sticky="ew", padx=2, pady=5)

    card = TradeCard(cardContainer, trades[0])
    card.grid(row=0, column=2, sticky="ew", padx=2, pady=5)

    #vertical dummy data
    card = TradeCard(cardContainer, trades[1])
    card.grid(row=1, column=0, sticky="ew", padx=2, pady=5)

    card = TradeCard(cardContainer, trades[2])
    card.grid(row=2, column=0, sticky="ew", padx=2, pady=5)








