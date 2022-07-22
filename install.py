import sqlite3,os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.ttk import Progressbar
import time
btn = Button
label = Label
entry = Entry
text = Text
listbx=Listbox
description="""
Database using sql import\nSQLITE3
            """
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def finished():
    for i in root.winfo_children(): i.pack_forget()
    label(root, text="Database Installed", font=("Arial", 25)).pack()
    ttk.Separator(root, orient=HORIZONTAL).pack(fill='x')
    label(root, text="Database was successfully installed.", font=("Arial", 20)).pack(fill=X)
    ttk.Separator(root, orient=HORIZONTAL).pack(fill='x')
    btn(root, text="Exit", command=quit, font=("Arial", 15)).pack(side=RIGHT, anchor=SE, padx=1, pady=1)
    root.bind("<Escape>", quit)
    root.bind("<Return>", quit)


def step():
    for i in range(10):
        root.update_idletasks()
        pb1['value'] += 10

        time.sleep(.5)
    btn(root, text="Continue", command=finished, font=("Arial", 15)).pack(side=RIGHT, anchor=SE, padx=1, pady=1)
def install(event=None):
    for i in root.winfo_children(): i.pack_forget()

    label(root, text="Database Installing", font=("Arial", 25)).pack()
    ttk.Separator(root, orient=HORIZONTAL).pack(fill='x')
    label(root, text="Database is being installed.\n\n", font=("Arial", 20)).pack(fill=X)
    global pb1
    pb1 = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
    pb1.pack(fill=X)
    step()
    ttk.Separator(root, orient=HORIZONTAL).pack(fill='x')

    root.bind("<Escape>", quit)
    root.bind("<Return>", quit)

    if not os.path.exists("db.db"):
        open("db.db", 'x')
    else:
        pass
    db = sqlite3.connect("db.db")
    cu = db.cursor()
    cu.execute("CREATE TABLE STUDENTS (name TEXT, grade int,NumberofClasses int,ClassGrades TEXT)")
    cu.close()
    db.close()


def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

if is_admin():
    global root
    root = Tk()
    root.title("Install School Database")
    root.geometry("500x500")
    center(root)
    label(root, text="Install Database", font=("Arial", 25)).pack()
    ttk.Separator(root, orient=HORIZONTAL).pack(fill='x')
    label(root, text=description, font=("Arial", 20)).pack(fill=X)
    ttk.Separator(root, orient=HORIZONTAL).pack(fill='x')
    btn(root, text="Install", command=install, font=("Arial", 15)).pack(side=RIGHT, anchor=SE, padx=1, pady=1)
    btn(root, text="Cancel", command=quit, font=("Arial", 15)).pack(side=RIGHT, anchor=SE, padx=1, pady=1)
    root.bind("<Escape>", quit)
    root.bind("<Return>", install)
    root.mainloop()

else:
    # Re-run the program with admin rights
    mb.showerror(title="Install Failure",
                 message="Administrator Permissions are required to install the application as it is installed to C:\ which is a system drive and folder and it requires these permissions.")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

