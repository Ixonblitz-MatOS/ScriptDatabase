#Imports
import sqlite3
import tkinter as tk
#end
#int float str bytes bytearray tuple list(array) dict
#pass does nothing
#INSERT INTO table_name (column1, column2, column3, ...)
#VALUES (value1, value2, value3, ...);
class sqlfile:
    def __init__(self,sqlFile:str):
        self.file=sqlite3.connect(sqlFile)
        self.cursor=self.file.cursor()
    def dictToString(self,dicts:dict):
        finalString=""
        for i in dicts.keys():
            finalString+=f"{i}:{dicts[i]};"
        return finalString
    def StringtoDict(self,string:str):
        finaldict=dict()
        for i in string.split(";"):
            finaldict[i.split(":")[0]]=i.split(":")[1]
        return finaldict
    def addStudentInfo(self, StudentName: str, Grade: int, NumberOfClasses: int, ClassGrades: dict): self.addInfo(
        StudentName, Grade, NumberOfClasses, ClassGrades)
    def getStudentInfo(self,StudentName:str):
        sqlite_select_query = f"""SELECT * from STUDENTS WHERE name='{StudentName}'"""
        self.cursor.execute(sqlite_select_query)
        records = self.cursor.fetchall()
        for rows in records:
            return rows[0], rows[1], rows[2], rows[3]
    def addInfo(self,StudentName:str,Grade:int,NumberOfClasses:int,ClassGrades:dict):
        self.cursor.execute(f"INSERT INTO STUDENTS (name, grade,NumberofClasses,ClassGrades);VALUES ({StudentName},{Grade},{NumberOfClasses},{self.dictToString(ClassGrades)});")
    def __del__(self):self.cursor.close()
    def __delete__(self, instance):self.cursor.close()
class commandLineApp:
    def __init__(self):
        self.sql=sqlfile("db.db")
    def addStudentInfo(self,StudentName:str,Grade:int,NumberOfClasses:int,ClassGrades:dict):pass

    def getStudentInfo(self):
        Studentname=input("What is your name?")
        StudentGrade = int(input("What is your grade"))
        numberOfClasses=int(input("How many classes do you take"))
        i=1
        classes=dict()
        while i<=numberOfClasses:
            grade=input(f"What is your grade for class {i}")
            classes[i]=grade
            i+=1
        #GPA_dict = dict()
        #{"":4.0}
        #if grade is


    def _gpa_calculator(self,grades:list):
        points = 0
        i = 0

        grade_c = {"A": 4, "A-": 3.67, "B+": 3.33, "B": 3.0, "B-": 2.67, "C+": 2.33, "C": 2.0, "C-": 1.67, "D+": 1.33,
                   "D": 1.0, "F": 0}
        if grades != []:
            for grade in grades:
                points += grade_c[grade]
            gpa = points / len(grades)
            return gpa
        else:
            return None



if __name__ == "__main__": #makes sure python is properly configured
    apps=commandLineApp()



