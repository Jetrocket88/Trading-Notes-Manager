from tkinter import ttk
import tkinter as tk

import styles

def makeScrollableText(parent, height=40, width=None, font=None):

    container = ttk.Frame(parent)
    textWidget = tk.Text(container, height=height, wrap="word")
    if width:
        textWidget.configure(width=width)
    if font:
        textWidget.configure(font=font)


    scrollbar = ttk.Scrollbar(container, orient="vertical", command=textWidget.yview)
    textWidget.configure(yscrollcommand=scrollbar.set)

    textWidget.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return container, textWidget 


def makeInput(parent, inputDict, name, width=40, height=5, multiline=False, font=None):
    if multiline:
        # Returns container frame + text widget
        container, widget = makeScrollableText(parent, width=width, height=height, font=font)
        inputDict[name] = widget
        return container
    else:
        widget = ttk.Entry(
            parent,
            width=width,
        )
        inputDict[name] = widget
        return widget

def makeComboBox(container, values):
    combo = ttk.Combobox(
        container,
        values=values,
        state="readonly"
    )
    combo.current(0)
    return combo


