#!/usr/bin/python

PROGRAM_NAME = "students-Marks-Entry"
VERSION = '0.2.0'

import tkinter as tk
from tkinter import scrolledtext

s=[]    # Insert subjects names
n=[]    # Insert marks NOTE = this is a list of tuples in the from of (subject of type str, marks of that subject in type float)
u=1    # use to create a document
y=1 # use to assign numbers to the document
t=1 # use to filter the correct numbers

'''
# Create document or not
while u>0:
    print('Do you want to create a new document to store results? (y/n)')
    choice=input('')
    if choice.lower()=='y':
        AF=open("Marks.txt","w")
        AF.close()
        break
    elif choice.lower()=='n':
        break
    else:
        continue
    
'''


root = tk.Tk()
root.title(PROGRAM_NAME)
canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

# window to ask studen's name
root.withdraw()
nameWin = tk.Toplevel()
nameWin.geometry('400x150')
nameInLabel = tk.Label(nameWin, text="Enter student's name below", pady=10)
nameInLabel.place(anchor='n', relx=0.5)
nameInEntry = tk.Entry(nameWin)
nameInEntry.place(width=380, height=40, y=50, x=10)
p = "empty"
def setStudName(name):
    if name != "":
        p = name
        root.title(p)
        root.deiconify()
        nameWin.destroy()
nameInBtn = tk.Button(nameWin, text="Submit", command=lambda:setStudName(nameInEntry.get()))
nameInBtn.place(anchor="c", relx=0.5, y=120, width=100, height=50)

'''
p=input('Enter Student Name: ')

# Open a text document
AF=open("Marks.txt","a")
# Insert the Student name into document
AF.write('{0}) Student Name: {1}\n'.format(y,p))
AF.close()
'''

subjectsBoard = scrolledtext.ScrolledText(root, font=("Liberation Serief", 15))

_Minimum_ = None
_Maximum_ = None
_Total_ = None
_Avarage_ = None

def Maximum():
    a = n
    Max=a[0][1]
    for i in range(1,len(a)):
        if a[i][1]>Max:
            Max=a[i][1]
    global _Maximum_
    _Maximum_ = Max
    return Max

def Minimum():
    a = n
    Min=a[0][1]                                                                                          
    for i in range(1,len(a)):
        if a[i][1]<Min:
            Min=a[i][1]
    global _Minimum_
    _Minimum_ = Min
    return Min

def Total():
    a = n
    tot=a[0][1]
    for i in range(1,len(a)):
        tot+=a[i][1]
    global _Total_
    _Total_ = tot
    return tot

def Avarage():
    a = n
    avg=0
    tot=Total()
    avg=float(tot)/(len(a))
    global _Avarage_
    _Avarage_ = avg
    return avg

MaxLabel = tk.Label(root, text=f"Maximum:\t {_Maximum_}")
MinLabel = tk.Label(root, text=f"Minimum:\t {_Minimum_}")
TotalLabel = tk.Label(root, text=f"Total:\t\t {_Total_}")
AvgLAbel = tk.Label(root, text=f"Avarage:\t\t {_Avarage_}")

def EditSubjects(name, score, win):
    if name != None and name != "" and score != None:
        n.append((name, score))
        subjectsBoard.configure(state='normal')
        subjectsBoard.insert(tk.INSERT, f"\n{name}\t{score}")
        subjectsBoard.configure(state='disabled')
        MaxLabel.configure(text=f"Maximum:\t {Maximum()}")
        MinLabel.configure(text=f"Minimum:\t {Minimum()}")
        TotalLabel.configure(text=f"Total:\t\t {Total()}")
        AvgLAbel.configure(text=f"Avarage:\t\t {Avarage()}")
        win.destroy()

def AddNewSubject():
    subjectWin = tk.Toplevel()
    subjectWin.grab_set()
    subjectWin.transient(root)
    subjectNameInLabel = tk.Label(subjectWin, text="Enter subject name", padx=10, pady=10)
    subjectScoreInLabel = tk.Label(subjectWin, text="Enter marks for that subject", padx=10, pady=10)
    subjectNameInEntry = tk.Entry(subjectWin)
    subjectScoreInEntry = tk.Entry(subjectWin)
    
    def getScore():
        try:
            score = float(subjectScoreInEntry.get())
            return score
        except Exception:
            return None
    
    confirmBtn = tk.Button(subjectWin, text="add subject", padx=10, pady=10, command=lambda:EditSubjects(subjectNameInEntry.get(), getScore(), subjectWin))
    backBtn = tk.Button(subjectWin, text="cancel", padx=10, pady=10, command=subjectWin.destroy)
    
    subjectNameInLabel.pack()
    subjectNameInEntry.pack()
    subjectScoreInLabel.pack()
    subjectScoreInEntry.pack()
    confirmBtn.pack()
    backBtn.pack()
    

def RmAll():
    #TODO
    pass

subjectsNote = tk.Label(root, text="Subjects")
subjectsNote.place(anchor='c', relx=0.25, y=20)

subjectsBoard.place(x=10, y=40, relheight=0.75, relwidth=0.5)
subjectsBoard.configure(state='disabled')

addSubjectBtn = tk.Button(root, padx=10, pady=10, text="Add new subject", command=AddNewSubject)
addSubjectBtn.place(anchor='c', relx=0.125, rely=0.925, width=125, height=40)

rmAllSubjectsBtn = tk.Button(root, padx=10, pady=10, text="clear all subjects", command=lambda:RmAll)
rmAllSubjectsBtn.place(anchor='c', relx=0.375, rely=0.925, width=125, height=40)
        
def SaveToDisk():
    #TODO
    pass

MaxLabel.place(anchor='c', height=30, width=200, relx=0.75, rely=0.1)
MinLabel.place(anchor='c', height=30, width=200, relx=0.75, rely=0.2)
TotalLabel.place(anchor='c', height=30, width=200, relx=0.75, rely=0.3)
AvgLAbel.place(anchor='c', height=30, width=200, relx=0.75, rely=0.4)

saveToDiskBtn = tk.Button(root, text="Save data to disk", command=lambda:SaveToDisk)
EXITbtn = tk.Button(root, text="Exit", command=exit)

saveToDiskBtn.place(anchor='c', height=40, width=200, relx=0.75, rely=0.65)
EXITbtn.place(anchor='c', height=40, width=100, relx=0.75, rely=0.85)

# h=int(input('How many subjects do you have? '))
# for i in range(1,h+1):
#     m=input('Enter Subject {0} name: '.format(i))
#     s.append(str(m))
    
# for i in range(h):
#     while t>0:
#     # Input subjects marks
#         x=input('Enter {0} marks: '.format(s[i]))
    
#         # Check the compatibility of the input
#         if int(x)>=0:
#             if int(x)<=100:
#                 t+=1
#                 # Assign values to the list 'n'
#                 n.append(int(x))
#                 break
#             else:
#                 print("You can't input more than 100 values")
#                 continue
        
#         elif int(x)<0:
#             print("You can't input negative values")
#             continue
# # How to return to the while condition when input "String"???
#         else:
#             print("You can only input numbers")
#             continue


# # Insert the Subject name and marks into document
# AF=open("Marks.txt","a")
# for p in range(h):
#     i=0
#     AF.write('{0}: {1}\n'.format(s[p],n[i]))
#     i+=1
# AF.close()

# Create loop to the infinity
'''
while True:
    # Display the options
    print("What do you want? \n1) Max \n2) Min \n3) Total \n4) Avg \n5) Count \n6) New Entry \n7) Finish")
    # input only the numbers of the above options
    c=int(input("Enter number: "))

    # Find Max
    if c==1:

        print(func(n))

        # Open a text document
        AF=open("Marks.txt","a")
        # Insert the max into document
        AF.write('* Max: {0}\n'.format(Max))
        AF.close()

    # Find Min        
    elif(c==2):

        print(func(n))
        # Open a text document
        AF=open("Marks.txt","a")
        # Insert the max into document
        AF.write('* Min: {0}\n'.format(Min))
        AF.close()

    # Find Total
    elif(c==3):

        print(func(n))
        # Open a text document
        AF=open("Marks.txt","a")
        # Insert the max into document
        AF.write('* Total: {0}\n'.format(tot))
        AF.close()

    # Find Avg
    elif(c==4):

        print(func(n))
        # Open a text document
        AF=open("Marks.txt","a")
        # Insert the max into document
        AF.write('* Avg: {0}\n'.format(avg))
        AF.close()
        
    # Find Count
    elif(c==5):
        print(' Subject count is {0}\n'.format(len(n)))
        # Open a text document
        AF=open("Marks.txt","a")
        # Insert the max into document
        AF.write('* Subject count: {0}\n'.format(len(n)))
        AF.close()

    # Finish the process
    elif c==7:
        break
    

    # Delete the current list
    elif c==6:
        del n   # Delete previous 'n'
        del s   # Delete previous 's'
        
        # Create a new list 'n' and 's'
        s=[]    # Insert subjects names
        n=[]    # Insert marks
        t=1

        y=y+1   # use to update numbers in document
        p=input('\nEnter Student Name: ')
        
        # Open a text document
        AF=open("Marks.txt","a")
        # Insert the Student name into document
        AF.write('\n{0}) Student Name: {1}\n'.format(y,p))
        AF.close()
        h=int(input('How many subjects do you have? '))
        
        for i in range(1,h+1):
            m=input('Enter Subject {0} name: '.format(i))
            s.append(str(m))
            
        for i in range(h):
            while t>0:
                # Input new subjects marks
                x=input('Enter {0} marks: '.format(s[i]))

                # Check the compatibility of the input
                if int(x)>=0:
                    if int(x)<=100:
                        t+=1
                        # Assign values to the list 'n'
                        n.append(int(x))
                        break
                    else:
                        print("You can't input more than 100 values")
                        continue
        
                elif int(x)<0:
                    print("You can't input negative values")
                    continue
                                                                                                    # How to return to the while condition when input "String"
                else:
                    print("You can only input numbers")
                    continue

            # Insert the Subject name and marks into document
            AF=open("Marks.txt","a")
            for p in range(h):
                i=0
                AF.write('{0}: {1}\n'.format(s[p],n[i]))
                i+=1
            AF.close()
'''

tk.mainloop()
