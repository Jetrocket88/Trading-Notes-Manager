from tkcalendar import Calendar
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
from turtle import width 

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

def makeStaticLabel(root, container, text, fontSize=None, width=30):
    newFont = font.Font(root=root, font=styles.getDefaultFont())
    if fontSize is not None:
        newFont.configure(size=fontSize)

    temp = ttk.Label(
        container,
        text=text,
        font=newFont,
    )
    temp.configure(width=width)
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


def setPopupOpenPosition(root, popup, width=None, height=None):
    # Wait for the popup to finish drawing so we can get its real size
    popup.update_idletasks()

    # Calculate center position relative to the parent window
    rootX = root.winfo_x()
    rootY = root.winfo_y()
    rootW = root.winfo_width()
    rootH = root.winfo_height()
    popupW = popup.winfo_reqwidth()
    popupH = popup.winfo_reqheight()

    x = rootX + (rootW // 2) - (popupW // 2)
    y = rootY + (rootH // 2) - (popupH // 2)

    if width is None or height is None:
        popup.geometry(f"+{x}+{y}")
    else:
        popup.geometry(f"{width}x{height}+{x}+{y}")



def openPopup(root, title, dim):
    popup = tk.Toplevel(root)
    popup.title(title)

    #position
    #setPopupOpenPosition(root, popup, dim[0], dim[1])
    popup.geometry(f"{dim[0]}x{dim[1]}+{875}+{300}")
    popup.protocol("WM_DELETE_WINDOW", lambda: exitPopup(popup))

    popup.transient(root)
    popup.grab_set()
    popup.resizable(False, False)

    popup.configure(bg=styles.BACKGROUND_COLOR)
    
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
    main_frame = ttk.Frame(parent)
    main_frame.pack(fill="both", expand=True)
    
    canvas = tk.Canvas(main_frame, bg=styles.BACKGROUND_COLOR, highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)
    
    scrollbar = ttk.Scrollbar(
        main_frame, 
        orient="vertical", 
        command=canvas.yview,
        style="Invisible.Vertical.TScrollbar"
    )
    scrollbar.pack(side="right", fill="y")
    
    canvas.configure(yscrollcommand=scrollbar.set)
    
    container = ttk.Frame(canvas, padding=padding)
    canvas_window = canvas.create_window((0, 0), window=container, anchor="nw")
    
    def configure_scroll(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(canvas_window, width=canvas.winfo_width())
    
    container.bind("<Configure>", configure_scroll)
    canvas.bind("<Configure>", configure_scroll)
    
    def on_mousewheel(event):
        if event.delta > 0:
            if canvas.yview()[0] > 0.0:
                canvas.yview_scroll(-1, "units")
        else:
            if canvas.yview()[1] < 1.0:
                canvas.yview_scroll(1, "units")
    
    canvas.bind_all("<MouseWheel>", on_mousewheel)
    
    return container 


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

def makeSpinBox(popup, range, format, variable, row, column):
    spin = ttk.Spinbox(popup, 
                       from_=range[0],
                       to=range[1], 
                       width=5,
                       format=format,
                       textvariable=variable,
                       state="readonly",
                       )
    spin.grid(row=row, column=column, padx=(0, 10), pady=5)
    return spin


def openCalendarPopup(root, dateEntryWidget):
    popup = tk.Toplevel(root)
    popup.title("Select a Date and Time")
    popup.transient(root)
    popup.grab_set()
    popup.resizable(False, False)
    popup.configure(bg=styles.BACKGROUND_COLOR)

    popup.geometry(f"+{875}+{300}")

    cal = Calendar(popup, date_pattern="yyyy-mm-dd", **styles.getCalendarStyle())
    cal.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    hourLabel = makeStaticLabel(root, popup, "Hour: (0-23)")
    hourLabel.grid(row=1, column=0, padx=(10, 5), pady=5)

    minuteLabel = makeStaticLabel(root, popup, "Minute: (0-59)")
    minuteLabel.grid(row=2, column=0, padx=(10, 5), pady=5)

    hourVar = tk.StringVar(value="11")
    minuteVar = tk.StringVar(value="59")

    makeSpinBox(popup, (0, 23), "%02.0f", variable=hourVar, row=1, column=2)
    makeSpinBox(popup, (0, 59), "%02.0f", variable=minuteVar, row=2, column=2)

    timeGuideLabel = makeStaticLabel(root, popup, "Please Note! Use 24h time")
    timeGuideLabel.grid(row=3, column=0, sticky="ew", columnspan=3, pady=5)
    timeGuideLabel.configure(foreground="gray38")

    def confirmDate():
        date = cal.selection_get().strftime("%Y-%m-%d")
        hour = hourVar.get().zfill(2)
        minute = minuteVar.get().zfill(2)
        dateEntryWidget.delete(0, tk.END)
        dateEntryWidget.insert(0, f"{date} {hour}:{minute}")
        popup.destroy()

    ttk.Button(popup, text="Confirm", command=confirmDate).grid(row=4, column=0, columnspan=3, pady=(5, 15))


