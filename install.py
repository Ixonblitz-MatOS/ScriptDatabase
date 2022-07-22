import sqlite3,os
from tkinter import *
btn = Button
label = Label
entry = Entry
text = Text
def install():
    if not os.path.exists("db.db"):
        open("db.db",'x')
    else: pass
    db=sqlite3.connect("db.db")
    cu=db.cursor()
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
root=Tk()
root.title("Install School Database")
root.geometry("500x500")
center(root)
label(root,text="Install Database",font=("Arial",25)).pack()

root.mainloop()