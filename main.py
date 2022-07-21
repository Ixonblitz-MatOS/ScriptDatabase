#Imports
import sqlite3 as sql
import tkinter as tk
#end
#int float str bytes bytearray tuple list(array)
class app:
    def __init__(self,title:str,size:str,resizable:tuple):
        if len(resizable)>2: raise Exception("Resizable must be 2 integers")
        self.window=tk.Tk()
        self.window.title(title)
        self.window.geometry(size)
        self.window.resizable(resizable[0],resizable[1])



    def run(self):self.window.mainloop()