from tkinter import *
a=Tk()
etry=Entry(a,width=50,borderwidth=2)
etry.pack()
etry.insert(0,"Enter your id number")
def click():
    L=Label(a,text="Hey  "+etry.get()+",  supp...").pack()
b=Button(a,text="Enter your id",bg="skyblue",command=click).pack()

a.mainloop()
