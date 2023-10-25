from tkinter import *
import sys
root=Tk()
#Creating a Library Management System
root.geometry("3000x700")
root.title("Library Management System")
upperFrame=Frame(root,bg='red',borderwidth=7)
upperFrame.pack(padx=0)
def makeElement(title,row,col):
    Label(inf,text=title,font='arial 14 bold',bg='lightgreen').grid(row=row,column=col,padx=20,pady=3)
    Entry(inf,width=30).grid(row=row,column=col+1,padx=20,pady=2)

def insert_book():
    lbx.insert(ACTIVE,"Python Programming")
def exitfunc():
    sys.exit(0)
    

Label(upperFrame,text="Library Management System",font=("arial",55,'bold')).pack()
middle=Frame(root,borderwidth=8)
middle.pack(anchor='center')
inf=Frame(middle,highlightbackground='red',highlightcolor="red", highlightthickness=2,bg='lightgreen')
inf.pack(side='left',anchor='w')
book_details=Frame(middle,highlightbackground='red',highlightcolor="red", highlightthickness=2)
book_details.pack(side='right')
Label(book_details,text="Book Details",font='arial 13 bold',fg='white',bg='lightgreen').pack()
lbx=Listbox(book_details,font="arial 12 bold",width=35,height=14)
lbx.pack(side='left')
lbx.insert(END,"Naman Bansal")
lbx_student_details=Listbox(book_details,font="arial 12 bold",width=45,height=14)
lbx_student_details.pack()
lbx_student_details.insert(ACTIVE,"Name-Naman Bansal")
lbx_student_details.insert(ACTIVE,"Name-Naman Bansal")
lbx_student_details.insert(ACTIVE,"Name-Naman Bansal")
lbx_student_details.insert(ACTIVE,"Name-Naman Bansal")
my_buttons=Frame(root,borderwidth=2)
my_buttons.pack(anchor='n')
Button(my_buttons,text="Issue Book",fg='white',bg='lightgreen',height=1,width=15,font='arial 13 bold',highlightbackground='red',highlightcolor="red", highlightthickness=2).pack(side='left',padx=25)
Button(my_buttons,text="Add Book",fg='white',bg='lightgreen',height=1,width=15,font='arial 13 bold',highlightbackground='red',highlightcolor="red", highlightthickness=2).pack(side='left',padx=25)
Button(my_buttons,text="Return Book",fg='white',bg='lightgreen',height=1,width=15,font='arial 13 bold',highlightbackground='red',highlightcolor="red", highlightthickness=2).pack(side='left',padx=25)
Button(my_buttons,text="Know Student",fg='white',bg='lightgreen',height=1,width=15,font='arial 13 bold',highlightbackground='red',highlightcolor="red", highlightthickness=2).pack(side='left',padx=25)
Button(my_buttons,text="Exit",fg='white',bg='lightgreen',height=1,width=15,font='arial 13 bold',highlightbackground='red',highlightcolor="red", highlightthickness=2,command='exitfunc').pack(side='left',padx=25)

#Making Elements in Information Section
makeElement("Member Type:",0,0)
makeElement("Book Id:",0,2)
makeElement("PRN No.:",1,0)
makeElement("Book Title:",1,2)
#2nd Row
makeElement("ID No.:",2,0)
makeElement("Author Name:",2,2)
#4th Row
makeElement("First Name:",3,0)
makeElement("Date Borrowed:",3,2)
#5th Row
makeElement("Surname:",4,0)
makeElement("Date Due.:",4,2)
#6th Row
makeElement("Address 1:",6,0)
makeElement("Days on Book:",6,2)
#7th row
makeElement("Address 2:",7,0)
makeElement("Last Return Fine:",7,2)
#8th Row
makeElement("Post Code:",5,0)
makeElement("Date Over Due:",5,2)
#9th Row
makeElement("Mobile No.:",8,0)
makeElement("Actual Price:",8,2)



root.mainloop()