from tkinter import ttk
from tkinter import font

BACKGROUND_COLOR = "gray8"
FOREGROUND_COLOR = "whitesmoke"

UNUSED_BACKGROUND_COLOR = "gray34"

def getDefaultFont(root=None):
    return font.Font(
        root=root,
        family="Verdana",
        size=14,
        weight="normal"
    )

def initStyle(root):
    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        ".",
        background=BACKGROUND_COLOR,
        foreground=FOREGROUND_COLOR,
        font=getDefaultFont(root)
    )

    style.configure(
        "Unused_Window",
        background=UNUSED_BACKGROUND_COLOR,
        foreground=FOREGROUND_COLOR,
        font=getDefaultFont(root)
    )

    style.configure(
        "TEntry",
        foreground="black",
        fieldbackground= "white",
    )

    return style


