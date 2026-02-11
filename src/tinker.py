import tkinter as tk
from tkinter import ttk
import database as db


backgroundColor = "gray8"
textColor = "whitesmoke"
defaultFont = ("Verdana", 14, "normal")


def placeComponent(component, pos, root):
    root.update_idletasks()
    component.place(x=pos[0], y=pos[1], anchor="center")


def initWindow(width, height):
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    root.title("Trading Notes")
    root.geometry(f"{width}x{height}")
    root.protocol("WM_DELETE_WINDOWl", exitProgram)
    root.configure(bg=backgroundColor)
    return root


def makeStaticLabel(root, text, pos, color=None, backgroundColor=None, padX=0, padY=0):
    if backgroundColor is None:
        backgroundColor = root["bg"]

    if color is None:
        color = textColor

    temp = tk.Label(
        root,
        text=text,
        font=defaultFont,
        fg=color,
        bg=backgroundColor,
        padx=padX,
        pady=padY
    )
    placeComponent(temp, pos, root)
    return temp


def makeDynamicLabel(root, textVar, pos,
                     color=None, backgroundColor=None,
                     padX=0, padY=0):

    if backgroundColor is None:
        backgroundColor = root["bg"]

    if color is None:
        color = textColor

    temp = tk.Label(
        root,
        textvariable=textVar,
        font=defaultFont,
        fg=color,
        bg=backgroundColor,
        padx=padX,
        pady=padY
    )
    placeComponent(temp, pos, root)
    return temp


def exitProgram(root, conn):
    conn.close()
    root.destroy()


def makeTextVar(text):
    temp = tk.StringVar()
    temp.set(text)
    return temp


def updateTime(root, textVar):
    textVar.set(db.getNow())
    root.after(1000, updateTime, root, textVar)


def makeButton(root, text, command, pos,
               color=None, backgroundColor=None,
               padx=0, pady=0):

    if backgroundColor is None:
        backgroundColor = root["bg"]

    if color is None:
        color = textColor

    button = tk.Button(
        root,
        text=text,
        command=command,
        bg=backgroundColor,
        fg=color,
        font=defaultFont,
        bd=2,
        highlightthickness=0,
        padx=padx,
        pady=pady
    )
    placeComponent(button, pos, root)
    return button
