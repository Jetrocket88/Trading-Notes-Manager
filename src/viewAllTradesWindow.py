import tinker
from tkinter import messagebox
import database


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
    counter = 1
    for trade in trades:
        tempL = tinker.makeStaticLabel(popup, container, f"Entry Date: {trade.entryDate}")
        tempL.grid(row=counter, column=0)
        tempL.configure(anchor="center")
        counter += 1
        #messagebox.showinfo("Testing", row)









