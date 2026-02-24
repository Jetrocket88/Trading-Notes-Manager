import tinker
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
    #assert len(rows) != 0, "Rows is length of 0"
    temp = 1
    for row in rows:
        tinker.makeStaticLabel(popup, container,f"{row.entryDate}, {row.bias}" ).grid(row=temp, column=0)
        temp += 1


    trades = database.readIntoClasses(rows)







