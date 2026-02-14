import tkinter as tk
from tkinter import ttk
from tkinter import font 

import database
import helpers
import styles


def initWindow(width, height, pos):
    root = tk.Tk()
    root.title("Trading Notes")

    root.geometry(f"+{pos[0]}+{pos[1]}")
    root.geometry(f"{width}x{height}")

    root.protocol("WM_DELETE_WINDOW", lambda: helpers.exit(database.connect(), root))
    root.configure(bg=styles.BACKGROUND_COLOR)
    return root

def makeStaticLabel(root, container, text, fontSize=None):
    newFont = font.Font(root=root, font=styles.getDefaultFont())
    if fontSize is not None:
        newFont.configure(size=fontSize)

    temp = ttk.Label(
        container,
        text=text,
        font=newFont,
    )
    return temp


def makeDynamicLabel(root, container, textVar, fontSize=None):

    newFont = font.Font(root=root, font=styles.getDefaultFont())
    if fontSize is not None:
        newFont.configure(size=fontSize)

    temp = ttk.Label(
        container,
        textvariable=textVar,
        font=newFont,
    )
    return temp

def makeTextVar(text):
    temp = tk.StringVar()
    temp.set(text)
    return temp


def updateTime(root, textVar):
    textVar.set(database.getNow())
    root.after(1000, updateTime, root, textVar)


def exitPopup(popup):
    popup.destroy()


def applyThemeRecursive(widget, style=None, bgColor=None):
    if isinstance(widget, ttk.Widget):
        if style is not None:
            widgetClass = widget.winfo_class()
            fullStyle = f"{style}.{widgetClass}"
            try:
                widget.configure(style=fullStyle)
            except tk.TclError:
                pass
        else:
            if bgColor is not None:
                try:
                    widget.configure(bg=bgColor)
                except tk.TclError:
                    pass
    for child in widget.winfo_children():
        applyThemeRecursive(child, style, bgColor)
    


def openPopup(root, title, dim):
    popup = tk.Toplevel(root)
    popup.title(title)

    #position
    popup.update_idletasks()
    x = root.winfo_x() + root.winfo_width()  // 2
    y = root.winfo_y() + root.winfo_height() // 2 - 90
    popup.geometry(f"{dim[0]}x{dim[1]}+{x}+{y}")

    popup.protocol("WM_DELETE_WINDOW", lambda: exitPopup(popup))

    popup.transient(root)
    popup.grab_set()
    popup.resizable(False, False)

    popup.configure(bg=styles.BACKGROUND_COLOR)

    #change root to have unused background color
    #applyThemeRecursive(root, "Unused Window", styles.UNUSED_BACKGROUND_COLOR)
    
    return popup

def makeButton(container, text, command, style="TButton"):
    button = ttk.Button(
        container,
        text=text,
        command=command,
        style=style
    )
    return button


def makeScrollableFrame(parent, padding=20):
    """Create a scrollable frame - COMPLETE WORKING VERSION"""
    # Main frame to hold everything
    main_frame = ttk.Frame(parent)
    main_frame.pack(fill="both", expand=True)
    
    # Canvas
    canvas = tk.Canvas(main_frame, bg=styles.BACKGROUND_COLOR, highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    
    # Configure canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Frame inside canvas
    container = ttk.Frame(canvas, padding=padding)
    canvas_window = canvas.create_window((0, 0), window=container, anchor="nw")
    
    # Update scrollregion when container size changes
    def configure_scroll(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(canvas_window, width=canvas.winfo_width())
    
    container.bind("<Configure>", configure_scroll)
    canvas.bind("<Configure>", configure_scroll)
    
    # Mousewheel scrolling
    def on_mousewheel(event):
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")
    
    canvas.bind_all("<MouseWheel>", on_mousewheel)
    
    # Manual update function
    def update_scroll():
        parent.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
    
    return container, update_scroll
