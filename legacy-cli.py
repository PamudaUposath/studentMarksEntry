
s=[]    # Insert subjects names
n=[]    # Insert marks
u=1    # use to create a document
y=1 # use to assign numbers to the document
t=1 # use to filter the correct numbers


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
    





p=input('Enter Student Name: ')

# Open a text document
AF=open("Marks.txt","a")
# Insert the Student name into document
AF.write('{0}) Student Name: {1}\n'.format(y,p))
AF.close()

h=int(input('How many subjects do you have? '))
for i in range(1,h+1):
    m=input('Enter Subject {0} name: '.format(i))
    s.append(str(m))
    
for i in range(h):
    while t>0:
    # Input subjects marks
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
                                                                                                    # How to return to the while condition when input "String"???
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



# Create loop to the infinity
while True:
    # Display the options
    print("What do you want? \n1) Max \n2) Min \n3) Total \n4) Avg \n5) Count \n6) New Entry \n7) Finish")
    # input only the numbers of the above options
    c=int(input("Enter number: "))

    # Find Max
    if c==1:
        def func(a):
            global Max
            Max=a[0]
            for i in range(1,len(a)):
                if a[i]>Max:
                    Max=a[i]
            return('The Max value is {0}\n'.format(Max))
        print(func(n))

        # Open a text document
        AF=open("Marks.txt","a")
        # Insert the max into document
        AF.write('* Max: {0}\n'.format(Max))
        AF.close()

    # Find Min        
    elif(c==2):
        def func(a):
            global Min
            Min=a[0]                                                                                           
            for i in range(1,len(a)):
                if a[i]<Min:
                    Min=a[i]
            return('The Min value is {0}\n'.format(Min))
        print(func(n))
        # Open a text document
        AF=open("Marks.txt","a")
        # Insert the max into document
        AF.write('* Min: {0}\n'.format(Min))
        AF.close()

    # Find Total
    elif(c==3):
        def func(a):
            global tot
            tot=a[0]
            for i in range(1,len(a)):
                tot=tot+a[i]
            return('The Total is {0}\n'.format(tot))
        print(func(n))
        # Open a text document
        AF=open("Marks.txt","a")
        # Insert the max into document
        AF.write('* Total: {0}\n'.format(tot))
        AF.close()

    # Find Avg
    elif(c==4):
        def func(a):
            global avg
            avg,tot=0,a[0]
            for i in range(1,len(a)):
                tot=tot+a[i]
                avg=float(tot)/(len(a))
            return('The Avarage is {0}\n'.format(avg))
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