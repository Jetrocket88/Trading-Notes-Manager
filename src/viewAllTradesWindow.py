import tinker


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
    titleLabel.grid(row=0, column=1)
    titleLabel.configure(anchor="center")



