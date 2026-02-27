import tinker
import styles
import tkinter as tk


def addLabel(popup, container, text, row, leftPad=10, sticky="w"):
    label = tinker.makeStaticLabel(popup, container, text)
    label.grid(row=row, column=0, pady=(10, 0), padx=leftPad, sticky=sticky)
    return label

def addHelp(popup, container, text, row, wrap=200, sticky="ns", column=1):
    helpLabel = tinker.makeStaticLabel(popup, container, text, fontSize=7)
    helpLabel.configure(foreground="gray38", wraplength=wrap)
    helpLabel.grid(row=row, column=column, pady=(0, 0), padx=(10, 10), sticky=sticky)

def addInput(container, inputDict, name, row, leftPad=10):
    input = tinker.makeInput( container, inputDict, name, multiline=False )
    input.grid(row=row, column=0, padx=(leftPad, 0), pady=(8, 10), sticky="ew")
    return input

def addButton(container, text, function, row):
    button = tinker.makeButton(container, text,  function)
    button.grid(row=row, column=2, pady=(0, 10))
    return button

def addTextarea(container, inputDict, name, row, leftPad=10, width=60, height=5):
    font = styles.getDefaultFont()
    font.configure(size=9)
    input = tinker.makeInput(container, inputDict, name, multiline=True, width=width, height=height)
    input.grid(row=row, column=0, padx=(leftPad, 0), pady=(8, 10), sticky="ew", columnspan=2)
    return input


def addCombo(container, list, inputDict, name, row, function, leftPad=10):
    combo = tinker.makeComboBox(container, list)
    combo.grid(column=0, row=row, sticky="ew", padx=(leftPad, 0), pady=(0, 0))
    combo.bind("<Button-1>", function)
    combo.bind("<FocusIn>", function)
    inputDict[name] = combo 
    return combo


def getDataFromWidget(widget):
    if isinstance(widget, tk.Text):
        return widget.get("1.0", "end-1c") 
    else:
        return widget.get()

