from tkinter import messagebox
import tinker as tk

def exit(connection, root):
    connection.close()
    root.destroy()


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

