from tkinter import *
root=Tk()
#Creating a Library Management System
root.geometry("3000x700")
root.title("Library Management System")
upperFrame=Frame(root,bg='red',borderwidth=7)
upperFrame.pack(padx=0)
Label(upperFrame,text="Library Management System",font=("arial",55,'bold')).pack()
middle=Frame(root,borderwidth=8)
middle.pack(anchor='center')
inf=Frame(middle,borderwidth=3)
inf.pack(side='left')
membertype=Label(inf,text="Member Type:").grid(row=0,column=0)
Entry(inf).grid(row=0,column=1,pady=4)
membertype=Label(inf,text="Book No.:").grid(row=0,column=2)
Entry(inf).grid(row=0,column=3,pady=4)
membertype=Label(inf,text="PRN NO.:").grid(row=1,column=0)
Entry(inf).grid(row=1,column=1,pady=4)
membertype=Label(inf,text="Book Title:").grid(row=1,column=2)
Entry(inf).grid(row=1,column=3,pady=4)
# Getting 3rd Row
membertype=Label(inf,text="Id NO.:").grid(row=2,column=0)
Entry(inf).grid(row=3,column=1,pady=4)
membertype=Label(inf,text="Author name:").grid(row=2,column=2)
Entry(inf).grid(row=3,column=3,pady=4)
# Getting 4th Row
membertype=Label(inf,text="Id NO.:").grid(row=3,column=0)
Entry(inf).grid(row=3,column=1,pady=4)
membertype=Label(inf,text="Author name:").grid(row=2,column=2)
Entry(inf).grid(row=1,column=3,pady=4)

# Next Row and Column



root.mainloop()