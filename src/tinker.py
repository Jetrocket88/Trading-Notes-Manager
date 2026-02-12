import tkinter as tk
from tkinter import ttk
from tkinter import font 

import database as db
import helpers as h


backgroundColor = "gray8"
textColor = "whitesmoke"
defaultFont = None

def setBackgrounds(widget, color):
    try:
        widget.configure(bg=color)
            
    except tk.TclError:
        pass
    for child in widget.winfo_children():
        setBackgrounds(child, color)

def getDefaultFont(root):
    global defaultFont
    if defaultFont is None:
        defaultFont = font.Font(
            root=root,
            family="Verdana",
            size=14,
            weight="normal"
        )
    return defaultFont

def placeComponentCenter(component, pos, root):
    root.update_idletasks()
    component.place(x=pos[0], y=pos[1], anchor="center")

def placeComponentCorner(component, pos, root):
    root.update_idletasks()
    component.place(x=pos[0], y=pos[1])

def initWindow(width, height, pos):
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    root.title("Trading Notes")

    root.geometry(f"+{pos[0]}+{pos[1]}")
    root.geometry(f"{width}x{height}")

    root.protocol("WM_DELETE_WINDOW", lambda: h.exit(db.connect(), root))
    root.configure(bg=backgroundColor)
    getDefaultFont(root)
    return root

def makeStaticLabel(root, text, pos, color=None, backgroundColor=None, padX=0, padY=0, fontSize=None):
    if backgroundColor is None:
        backgroundColor = root["bg"]

    if color is None:
        color = textColor

    newFont = font.Font(root=root, font=defaultFont)
    if fontSize is not None:
        newFont.configure(size=fontSize)

    temp = tk.Label(
        root,
        text=text,
        font=newFont,
        fg=color,
        bg=backgroundColor,
        padx=padX,
        pady=padY
    )
    placeComponentCenter(temp, pos, root)
    return temp


def makeDynamicLabel(root, textVar, pos,
                     color=None, backgroundColor=None,
                     padX=0, padY=0, fontSize=None):

    if backgroundColor is None:
        backgroundColor = root["bg"]

    if color is None:
        color = textColor

    newFont = font.Font(root=root, font=defaultFont)
    if fontSize is not None:
        newFont.configure(size=fontSize)

    temp = tk.Label(
        root,
        textvariable=textVar,
        font=newFont,
        fg=color,
        bg=backgroundColor,
        padx=padX,
        pady=padY
    )
    placeComponentCenter(temp, pos, root)
    return temp


def makeTextVar(text):
    temp = tk.StringVar()
    temp.set(text)
    return temp


def updateTime(root, textVar):
    textVar.set(db.getNow())
    root.after(1000, updateTime, root, textVar)


def makeButton(root, text, command, pos,
               color=None, backgroundColor=None,
               padx=0, pady=0, fontSize=None):

    if backgroundColor is None:
        backgroundColor = root["bg"]

    if color is None:
        color = textColor

    newFont = font.Font(root=root, font=defaultFont)
    if fontSize is not None:
        newFont.configure(size=fontSize)

    button = tk.Button(
        root,
        text=text,
        command=command,
        bg=backgroundColor,
        fg=color,
        font=newFont,
        bd=2,
        highlightthickness=0,
        padx=padx,
        pady=pady
    )

    placeComponentCenter(button, pos, root)
    return button

def exitPopup(root, popup):
    global backgroundColor
    setBackgrounds(root, backgroundColor)
    popup.destroy()


def openPopup(root, title, dim):
    global backgroundColor
    popup = tk.Toplevel(root)
    popup.title(title)

    #width and height
    popup.geometry(f"{dim[0]}x{dim[1]}")

    #position
    popup.update_idletasks()
    x = root.winfo_x() + root.winfo_width()  // 2
    y = root.winfo_y() + root.winfo_height() // 2 - 90
    popup.geometry(f"+{x}+{y}")

    popup.protocol("WM_DELETE_WINDOW", lambda: exitPopup(root, popup))

    style = ttk.Style()
    style.theme_use("clam")

    popup.transient(root)
    popup.grab_set()
    popup.resizable(False, False)

    setBackgrounds(root, "gray18")
    popup.configure(bg=backgroundColor)
    return popup

def makeScrollableText(root, pos, dim):

    container = tk.Frame(root, bg=root["bg"])
    container.place(x=pos[0], y=pos[1], width=dim[0], height=dim[1])

    text = tk.Text(
        container,
        wrap="word",
        bd=0,
        highlightthickness=1,
        relief="solid"
    )

    scrollbar = ttk.Scrollbar(container, orient="vertical", command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)

    text.place(x=0, y=0, width=dim[0]-15, height=dim[1])
    scrollbar.place(x=dim[0]-15, y=0, width=15, height=dim[1])

    return text


def makeInput(root, inputDict, name, pos, dims, multiline=False):
    if multiline:
        widget = makeScrollableText(root, pos, dims)
    else:
        widget = tk.Entry(root, width=dims[0])
        placeComponentCorner(widget, pos, root)
    inputDict[name] = widget
    return widget


