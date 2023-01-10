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

## Instructions For Legacy-cli mode:

* First insert all the details of the student(name,subject and marks).
* This program can get,\
&ensp;* max of the all subjects\
&ensp;* min of the all subjects\
&ensp;* total of the all subjects\
&ensp;* average\
&ensp;* count of the all subjects
* Finally genarate a text file including all the details of the student.

## Commands & Instructions:

>Do you want to create a new document to store results? (y/n)\
y --> Create a new text file name as "Marks" or overwrite the existing "Marks.txt" file\
n --> Never create a new file. But if there isn't any text file called "Marks", automatically create a "Mark.txt" file\

>Enter Student Name:\
--> Enter name of the student

>How many subjects do you have?\
--> Enter count of the subjects

>Enter Subject [number] name:\
--> According to the above input, you have to insert subject names

>Enter [subject name] marks:\
--> Enter marks according to the [subject name]

>What do you want?
>1) Max
>2) Min
>3) Total
>4) Avg
>5) Count
>6) New Entry
>7) Finish
>Enter number:
--> 1] max marks of the all subjects\
--> 2] min of the all subjects\
--> 3] total of the all subjects\
--> 4] average\
--> 5] count of the all subjects\
--> 6] add a new student and his/her details\
--> 7] Save all the details inside the "Marks.txt" and terminate program