## Script Database

ScriptDatabase is a databasing system that can do the following:
- Take Student Name, grade, classes, grades 
- Save this data to a database using ```sqlite3```
- Retrieve and copy the data to clipboard 

ScriptDatabase is built in full python and uses the following python modules:
- Tkinter: The GUI module using TCL/TK Framework
- re: Used for Regex in ```builtins.py``` to create char class(redefining built in data types)
- Sqlite3: Used to read/write SQL databases to store students data.
- time: Used in ```install.py``` to keep ```tkinter.ttk.Progressbar``` running.
- os: Used in ```install.py``` top check if SQL database is existing.
- ctypes: Used in ```install.py``` alongside ```sys``` to request administrator privileges
- sys: Used in ```install.py``` alongside ```ctypes``` to request administrator privileges
<!--
### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```
-->
