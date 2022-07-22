import tkinter as tk
from main import sqlfile
btn = tk.Button
label = tk.Label
entry = tk.Entry
text = tk.Text
listbx=tk.Listbox

class app(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sql=sqlfile("db.db")
        self.cur=self.sql.cursor()
    def run(self): self.mainloop()
    def end(self): self.destroy()
    def hide(self): self.withdraw()
    def show(self): self.focus()
