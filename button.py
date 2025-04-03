from tkinter import *
a=Tk()
def click():
    Label1=Label(a,text="Hey...You clicked ",fg="red").grid(column=9,row=9)
Button=Button(a,text="Click on me",fg="black",bg="skyblue",command=click).grid(row=5,column=9)
a.mainloop()
