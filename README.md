# Students Marks Entry

**NOTE**

You need to have python installed for this program to work

Clone this repository

## Instructions for GUI mode:

This program depends on tkinter. So you need to install it.

Usually this can be achieved by running `pip install tkinter` in a command line

but depending on your Operating System this may or may not work

For example sometimes you will need to install `python-tk` or `python-tkinter` or similar package using your package-manager in most linux distributions

after installing tkinter,

cd into the repository using the command-line and execute the `students.marks.entry.py` 

or just simply execute the script `students.marks.entry.py` in python using a graphical user interface if your operating system supports such actions

## BUILD instructions for GUI

install pyinstaller usign pip `pip install pyinstaller`

cd into the folder using `cd students-Marks-Entry`

execute the command `pyinstaller.exe .\students.marks.entry.py -w --onefile --name="Students Marks Entry"`

Your executable binary will be located at `Student Marks Entry.exe`

## Instructions For Legacy-cli mode:

* First insert all the details of the student(name,subject and marks).
* This program can get,\
&ensp;* max of the all subjects\
&ensp;* min of the all subjects\
&ensp;* total of the all subjects\
&ensp;* average\
&ensp;* count of the all subjects
* Finally genarate a text file including all the details of the student.
