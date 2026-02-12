from tkinter import messagebox
import tinker as tk

WIDTH = 800
HEIGHT = 600
CENTER = (WIDTH / 2, HEIGHT / 2)

def exit(connection, root):
    connection.close()
    root.destroy()


def addATrade():
    pass


def centerOffset(x, y, width, height):
    CENTER = (width // 2, height // 2)
    return (CENTER[0] + x, CENTER[1] + y)

def topOffset(y, height):
    return -height/2 + y

def leftOffset(x, width):
    return -width/ 2 + x


def screenRes():
    try:
        root = tk.initWindow(1, 1, (0, 0))
        root.withdraw()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.destroy()
        return width, height
    except Exception as e:
        messagebox.showerror("Windows Screen Error", str(e))

