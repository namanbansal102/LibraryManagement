from tkinter import *
import sys
import time
from datetime import datetime,date,timedelta
todays_date=date.today()
dt=datetime.now()
from db import fetchData,insertData,updateBook,returnUpdateBook
from studentdb import insertStudentData,fetchStudentData,updateStudentData,returnStudentBookData,returnSpecifictudentData
root=Tk()
#Creating a Library Management System
root.geometry("3000x700")
root.title("Library Management System")
bookenteridvar=IntVar()
bookenternamevar=StringVar()
bookenterquantityvar=IntVar()
bookid=IntVar()
booktitle=StringVar()
studentId=IntVar()
studentName=StringVar()
address=StringVar()
mobileNo=IntVar()
dateIssued=StringVar()
def addBook():
    print(bookenteridvar.get(),bookenternamevar.get(),bookenterquantityvar.get())
    res=insertData(int(bookenteridvar.get()),str(bookenternamevar.get()),int(bookenterquantityvar.get()),0)
    if res==0:
        Label(side_lower,text="Error",font='arial 12 bold',fg='red',bg='lightgreen').grid(row=3,column=1)
    else:
        Label(side_lower,text="Book Insert Successfully",font='arial 12 bold',fg='red',bg='lightgreen').grid(row=3,column=1)
upperFrame=Frame(root,bg='red',borderwidth=7)
upperFrame.pack(padx=0)
def makeElement(title,row,col,runvar):
    Label(inf,text=title,font='arial 14 bold',bg='lightgreen').grid(row=row,column=col,padx=20,pady=3)
    if runvar=="bookid":
        Entry(inf,width=30,textvariable=bookid).grid(row=row,column=col+1,padx=20,pady=2)
    elif runvar=="booktitle":
        Entry(inf,width=30,textvariable=booktitle).grid(row=row,column=col+1,padx=20,pady=2)
    elif runvar=="studentId":
        Entry(inf,width=30,textvariable=studentId).grid(row=row,column=col+1,padx=20,pady=2)
    elif runvar=="studentName":
        Entry(inf,width=30,textvariable=studentName).grid(row=row,column=col+1,padx=20,pady=2)
    elif runvar=="address":
        Entry(inf,width=30,textvariable=address).grid(row=row,column=col+1,padx=20,pady=2)
    elif runvar=="mobileNo":
        Entry(inf,width=30,textvariable=mobileNo).grid(row=row,column=col+1,padx=20,pady=2)
    elif runvar=="dateIssued":
        l=Entry(inf,width=30,textvariable=dateIssued)
        l.insert(1,string=f"{todays_date.day}/{todays_date.month}/{todays_date.year}")
        l.grid(row=row,column=col+1,padx=20,pady=2)

        
        

    
def exitfunc():
    pass
#Issue Book Function is Started
def issueBook():
    print("issue Button is Clicked")
    for bookdp in fetchData():
        if bookdp[0]==bookid.get():
            print("Book is Present")
            if bookdp[2]==bookdp[3]:
                print("Books are All Issued")
                break
            
            else:
                updateBook(bookid.get())
                for data in fetchStudentData():
                    print("The Value of data is",data)
                    if data[0]==studentId.get():
                        print(data[0])
                        print("Student Id Get equal to enter  Inout Id")
                        updateStudentData(studentId.get(),{"bookid":bookid.get(),"dateOfIssued":dateIssued.get()})
                        break
                else:
                    print(studentId.get(),studentName.get(),address.get(),mobileNo.get(),{"bookid":bookid.get(),"dateOfIssued":dateIssued.get()})
                    insertStudentData(studentId.get(),studentName.get(),address.get(),mobileNo.get(),str([{"bookid":bookid.get(),"dateOfIssued":dateIssued.get()}]))
            break
                
    else:
        print("Sorry Unable To Find Book With Respective Book Id")
#Issue Book Function Is Closed
def returnBook():
    for bookdp in fetchData():
        if bookdp[0]==bookid.get():
            print("Book is Present")
            if bookdp[2]==0:
                print("All Books Are Present")
                break
            
            else:
                for data in fetchStudentData():
                    print("The Value of data is",data)
                    if data[0]==studentId.get():
                        print(data[0])
                        print("Student Id Get equal to enter  Inout Id")
                        returnStudentBookData(studentId.get(),{"bookid":bookid.get(),"dateOfIssued":dateIssued.get()})
                        returnUpdateBook(bookid.get())
                        break
                else:
                    print("Unable To Fetch The Student")
                    break
            break
                
    else:
        print("Sorry Unable To Find Book With Respective Book Id")
def knowStudent():
    print("Know Student Function is Running")
    mydata=returnSpecifictudentData(studentId.get())
    lbx_student_details.insert(END,f'Student ID:{mydata[0]}')
    lbx_student_details.insert(END,f'Student Name:{mydata[1]}')
    lbx_student_details.insert(END,f"Address:{mydata[2]}")
    lbx_student_details.insert(END,f"Phone No.{mydata[3]}")
    print()
    if len(mydata)!=4:
        for key,value in mydata[4].items():
            lbx_student_details.insert(END,f"Id :{key}:Book Name{value}")
        
    pass
Label(upperFrame,text="Book Management System",font=("arial",55,'bold')).pack()
middle=Frame(root,borderwidth=8)
middle.pack(anchor='center')
inf=Frame(middle,highlightbackground='red',highlightcolor="red", highlightthickness=2,bg='lightgreen')
inf.pack(side='left',anchor='w')
book_details=Frame(middle,highlightbackground='red',highlightcolor="red", highlightthickness=2)
book_details.pack(side='right')
Label(book_details,text="Book Details",font='arial 13 bold',fg='white',bg='lightgreen').pack()
lbx=Listbox(book_details,font="arial 12 bold",width=35,height=14)
lbx.pack(side='left')

lbx_student_details=Listbox(book_details,font="arial 12 bold",width=45,height=14)
lbx_student_details.pack()
for row in fetchData():
    quantity=row[2]
    issued=row[3]
    if quantity-issued>0:
        lbx.insert(ACTIVE,row[1])
my_buttons=Frame(root,borderwidth=2)
my_buttons.pack(anchor='n')
Button(my_buttons,text="Issue Book",fg='white',bg='lightgreen',height=1,width=15,font='arial 13 bold',highlightbackground='red',highlightcolor="red", highlightthickness=2,command=issueBook).pack(side='left',padx=25)
Button(my_buttons,text="Return Book",fg='white',bg='lightgreen',height=1,width=15,font='arial 13 bold',highlightbackground='red',highlightcolor="red", highlightthickness=2,command=returnBook).pack(side='left',padx=25)
Button(my_buttons,text="Know Student",fg='white',bg='lightgreen',height=1,width=15,font='arial 13 bold',highlightbackground='red',highlightcolor="red", highlightthickness=2,command=knowStudent).pack(side='left',padx=25)
Button(my_buttons,text="Exit",fg='white',bg='lightgreen',height=1,width=15,font='arial 13 bold',highlightbackground='red',highlightcolor="red", highlightthickness=2,command='exitfunc').pack(side='left',padx=25)
lower_part=Frame(root,highlightbackground='green',highlightcolor="green", highlightthickness=2)
lower_part.pack()
side_lower=Frame(lower_part,highlightbackground='green',highlightcolor="green", highlightthickness=2,bg='lightgreen')
side_lower.pack(side='left')



Label(side_lower,text="BookId",font='arial 16 bold',fg='white',bg='lightgreen').grid(row=0,column=0)
Entry(side_lower,textvariable=bookenteridvar).grid(row=0,column=1)
Label(side_lower,text="Book Name",font='arial 16 bold',fg='white',bg='lightgreen').grid(row=1,column=0)
Entry(side_lower,textvariable=bookenternamevar).grid(row=1,column=1)
Label(side_lower,text="Quantity",font='arial 16 bold',fg='white',bg='lightgreen').grid(row=2,column=0)
Entry(side_lower,textvariable=bookenterquantityvar).grid(row=2,column=1)
Label(side_lower,text="",font='arial 12 bold',fg='red',bg='lightgreen').grid(row=3,column=1)
Button(side_lower,text="Add Book",fg='lightgreen',bg='white',height=1,width=15,font='arial 13 bold',highlightbackground='red',highlightcolor="red", highlightthickness=2,command=addBook).grid(row=4,column=1)

#Making Elements in Information Section
makeElement("Member Type:",0,0,"Student")
makeElement("Book Id:",0,2,"bookid")
makeElement("Book Title:",1,0,"booktitle")
#2nd Row
makeElement("ID No.:",1,2,"studentId")
makeElement("Student Name:",2,0,'studentName')
makeElement("Date Borrowed:",2,2,"dateIssued")
makeElement("Date Due.:",3,0,"nOne")
makeElement("Address 1:",3,2,"address")
makeElement("Days on Book:",4,0,"days")

getoverduelabel=Label(inf,text="Date Over Due",bg='lightgreen',font='arial 12 bold')
getoverduelabel.grid(row=4,column=1,padx=20,pady=2)
makeElement("Mobile No.:",5,0,"mobileNo")
root.mainloop()