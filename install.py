import sqlite3,os
if not os.path.exists("db.db"):
    open("db.db",'x')
else: pass
db=sqlite3.connect("db.db")
cu=db.cursor()
cu.execute("CREATE TABLE STUDENTS (name TEXT, grade int,NumberofClasses int,ClassGrades TEXT)")