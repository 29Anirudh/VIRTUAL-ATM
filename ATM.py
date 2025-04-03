from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as msg
a=Tk()
a.title("Virtual ATM")
a.geometry("830x700")
a.iconbitmap('C:/Users/Anirudh/Desktop/Tkinter/ATM-icon.ico')
#img=ImageTk.PhotoImage(Image.open("C:/Users/Anirudh/Desktop/Tkinter/ME.jpg"))
#Label=Label(image=img)
#Label.pack()
Acc_num=20202022200374
balance=20000
global pin
pin=1234
def elbm():#Primary
    acc_num=int(e.get())
    e.delete(0,END)
    if(acc_num==Acc_num):
        def Blbp():#PIN
            pin_check=int(e.get())
            e.delete(0,END)
            if(pin_check==pin):
                labpin=Label(mainframe,text="Your PIN is correct.You can do transactions.",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)#Correct PIN
                #TO COPY
                def b1():#WITHDRAW
                    label_wd=Label(mainframe,text="How much amount you want to withdraw?",width=50,height=25,bg="black",fg="white")#withdrawal
                    label_wd.grid(row=0,column=0)
                    msg.showinfo("Withdraw","Only 100,s and 500,s are available")#msgbox for withdrawal
                    global withdraw
                    def eb1():#Enter for withdraw
                        global balance
                        withdraw=int(e.get())
                        e.delete(0,END)
                        if(withdraw%100==0 and withdraw<=balance):
                            label_transaction=Label(mainframe,text="You have debited "+str(withdraw)+" amount from your account",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
                            balance=balance-withdraw
                        elif(withdraw>balance):
                            label_over=Label(mainframe,text="Insufficient funds",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
                        else:
                            label_cancel=Label(mainframe,text="Your transaction has been cancelled.Invalid amount of enter.",width=50,height=25,bg="black",fg="red").grid(row=0,column=0)
                    Bb1=Button(F3,text="Enter ",fg="black",bg="#808080",padx=10,pady=10,command=eb1,width=5,relief=RIDGE,font=('Sans',10,'bold'))#Entry button 1
                    Bb1.grid(row=3,column=0,padx=10,pady=5)
                def b2():#Balance_Enquiry
                    label_be=Label(mainframe,text="Your balance is "+str(balance),width=50,height=25,bg="black",fg="white").grid(row=0,column=0)#balance_enquiry
                def b3():#DEPOSIT
                    label_d=Label(mainframe,text="How much amount you want to deposit?",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)#deposit
                    msg.showinfo("Withdraw","Only 100,s and 500,s are acceptable")#msgbox for deposit
                    global deposit
                    def eb3():#enter for deposit
                        global balance
                        deposit=int(e.get())
                        e.delete(0,END)
                        if(deposit%100==0 and deposit<=20000):
                            label_deposit=Label(mainframe,text="You have credited "+str(deposit)+" amount to your account",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
                            balance+=deposit
                        elif(deposit>20000):
                            label_over1=Label(mainframe,text="You cannot deposit more than 20000",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
                        else:
                            label_cancel=Label(mainframe,text="Your transaction has been cancelled.Invalid amount of enter.",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
                    Bb3=Button(F3,text="Enter ",fg="black",bg="#808080",padx=10,pady=10,command=eb3,width=5,relief=RIDGE,font=('Sans',10,'bold'))#Entry button 2
                    Bb3.grid(row=3,column=0,padx=10,pady=5)
                def b4():#PIN CHANGE
                    lp=Label(mainframe,text="Enter your new 4-digit pin:",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
                    global pin_change
                    def enter():#enter for pin change
                        pin_change=e.get()
                        e.delete(0,END)
                        if(len(pin_change)==4):
                            lpc=Label(mainframe,text="Your pin has been changed.",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
                            pin=pin_change
                        else:
                            lpo=Label(mainframe,text="Invalid attempt.Cancelled.",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
                    Bb4=Button(F3,text="Enter ",fg="black",bg="#808080",padx=10,pady=10,command=enter,width=5,relief=RIDGE,font=('Sans',10,'bold'))#Entry button3 
                    Bb4.grid(row=3,column=0,padx=10,pady=5)
                #TOHERE
                #Buttons for user handling
                F1=LabelFrame(a)#First frame
                F1.grid(row=0,column=0,padx=10)
                b1=Button(F1,text="    Withdrawal    ",padx=60,pady=50,command=b1)#Withdrawal
                b1.grid(row =0,column=0,pady=5)
                b2=Button(F1,text="Balance enquiry",padx=60,pady=50,command=b2)#Balance enquiry
                b2.grid(row =1,column=0,pady=5)
                b3=Button(F1,text="        Deposit       ",padx=60,pady=50,command=b3)#Deposit
                b3.grid(row =2,column=0,pady=5)
                F1.configure(bg="#152238")
                F2=LabelFrame(a)#Second frame
                F2.grid(row=0,column=10,padx=10)
                b4=Button(F2,text="    Pin change    ",padx=60,pady=50,command=b4)#Pin change
                b4.grid(row =0,column=0,pady=5)
                b5=Button(F2,text="           Help         ",padx=60,pady=50)#Help
                b5.grid(row =1,column=0,pady=5)
                b6=Button(F2,text="           EXIT         ",padx=60,pady=50,command=a.destroy)#Exit
                b6.grid(row=2,column=0,pady=5)
                F2.configure(bg="#152238")
            else:
                labpin2=Label(mainframe,text="Incorrect PIN entered.Transcation cancelled.",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)#INVALID PIN
            
        lbp=Label(mainframe,text="Enter your 4-digit PIN:",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)#Pin_enter
        Blbp=Button(F3,text="Enter ",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,font=('Sans',10,'bold'),command=Blbp)#enter button
        Blbp.grid(row=3,column=0,padx=10,pady=5)
    else:
        lbp2=Label(mainframe,text="Invalid attempt",width=50,height=25,bg="black",fg="red").grid(row=0,column=0)#Wrong attempt of Acc.Num
#TO COPY
'''def b1():#WITHDRAW
    label_wd=Label(mainframe,text="How much amount you want to withdraw?",width=50,height=25,bg="black",fg="white")#withdrawal
    label_wd.grid(row=0,column=0)
    msg.showinfo("Withdraw","Only 100,s and 500,s are available")#msgbox for withdrawal
    global withdraw
    def eb1():#Enter for withdraw
        global balance
        withdraw=int(e.get())
        e.delete(0,END)
        if(withdraw%100==0 and withdraw<=balance):
            label_transaction=Label(mainframe,text="You have debited "+str(withdraw)+" amount from your account",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
            balance=balance-withdraw
        elif(withdraw>balance):
            label_over=Label(mainframe,text="Insufficient funds",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
        else:
            label_cancel=Label(mainframe,text="Your transaction has been cancelled.Invalid amount of enter.",width=50,height=25,bg="black",fg="red").grid(row=0,column=0)
    Bb1=Button(F3,text="Enter ",fg="white",bg="black",padx=10,pady=10,command=eb1)
    Bb1.grid(row=3,column=0,padx=10,pady=5)
def b2():#Balance_Enquiry
    label_be=Label(mainframe,text="Your balance is "+str(balance),width=50,height=25,bg="black",fg="white").grid(row=0,column=0)#balance_enquiry
def b3():#DEPOSIT
    label_d=Label(mainframe,text="How much amount you want to deposit?",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)#deposit
    msg.showinfo("Withdraw","Only 100,s and 500,s are acceptable")#msgbox for deposit
    global deposit
    def eb3():#enter for deposit
        global balance
        deposit=int(e.get())
        e.delete(0,END)
        if(deposit%100==0 and deposit<=20000):
            label_deposit=Label(mainframe,text="You have credited "+str(deposit)+" amount to your account",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
            balance+=deposit
        elif(deposit>20000):
            label_over1=Label(mainframe,text="You cannot deposit more than 20000",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
        else:
            label_cancel=Label(mainframe,text="Your transaction has been cancelled.Invalid amount of enter.",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
    Bb3=Button(F3,text="Enter ",fg="white",bg="black",padx=10,pady=10,command=eb3)
    Bb3.grid(row=3,column=0,padx=10,pady=5)
def b4():#PIN CHANGE
    lp=Label(mainframe,text="Enter your new 4-digit pin:",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
    global pin_change
    def enter():#enter for pin change
        pin_change=e.get()
        e.delete(0,END)
        if(len(pin_change)==4):
            lpc=Label(mainframe,text="Your pin has been changed.",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
            pin=pin_change
        else:
            lpo=Label(mainframe,text="Invalid attempt.Cancelled.",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)
    Bb4=Button(F3,text="Enter ",fg="white",bg="black",padx=10,pady=10,command=enter)
    Bb4.grid(row=3,column=0,padx=10,pady=5)
'''
#TOHERE
def num(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def clear():
    e.delete(0,END)
def bckspc():
    e.delete(len(e.get())-1,END)
#Buttons for user handling
F1=LabelFrame(a)#First frame
F1.grid(row=0,column=0,padx=10)
b1=Button(F1,text="    Withdrawal    ",padx=60,pady=50)#Withdrawal
b1.grid(row =0,column=0,pady=5)
b2=Button(F1,text="Balance enquiry",padx=60,pady=50)#Balance enquiry
b2.grid(row =1,column=0,pady=5)
b3=Button(F1,text="        Deposit       ",padx=60,pady=50)#Deposit
b3.grid(row =2,column=0,pady=5)
F1.configure(bg="#152238")
F2=LabelFrame(a)#Second frame
F2.grid(row=0,column=10,padx=10)
b4=Button(F2,text="    Pin change    ",padx=60,pady=50)#Pin change
b4.grid(row =0,column=0,pady=5)
b5=Button(F2,text="           Help         ",padx=60,pady=50)#Help
b5.grid(row =1,column=0,pady=5)
b6=Button(F2,text="           EXIT         ",padx=60,pady=50,command=a.destroy)#Exit
b6.grid(row=2,column=0,pady=5)
F2.configure(bg="#152238")
#Buttons from 0 to 9
F3=LabelFrame(a)
F3.grid(column=5,row=3)
B1=Button(F3,text="1",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,command=lambda:num(1),font=('Sans',10,'bold'))#1
B1.grid(row=0,column=0,padx=10,pady=5)
B2=Button(F3,text="2",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,command=lambda:num(2),font=('Sans',10,'bold'))#2
B2.grid(row=0,column=1,padx=10,pady=5)
B3=Button(F3,text="3",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,command=lambda:num(3),font=('Sans',10,'bold'))#3
B3.grid(row=0,column=2,padx=10,pady=5)
B4=Button(F3,text="4",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,command=lambda:num(4),font=('Sans',10,'bold'))#4
B4.grid(row=1,column=0,padx=10,pady=5)
B5=Button(F3,text="5",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,command=lambda:num(5),font=('Sans',10,'bold'))#5
B5.grid(row=1,column=1,padx=10,pady=5)
B6=Button(F3,text="6",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,command=lambda:num(6),font=('Sans',10,'bold'))#6
B6.grid(row=1,column=2,padx=10,pady=5)
B7=Button(F3,text="7",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,command=lambda:num(7),font=('Sans',10,'bold'))#7
B7.grid(row=2,column=0,padx=10,pady=5)
B8=Button(F3,text="8",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,command=lambda:num(8),font=('Sans',10,'bold'))#8
B8.grid(row=2,column=1,padx=10,pady=5)
B9=Button(F3,text="9",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,command=lambda:num(9),font=('Sans',10,'bold'))#9
B9.grid(row=2,column=2,padx=10,pady=5)
Bs=Button(F3,text="Enter ",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,font=('Sans',10,'bold'))#enter
Bs.grid(row=3,column=0,padx=10,pady=5)
B0=Button(F3,text="0",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,command=lambda:num(0),font=('Sans',10,'bold'))#0
B0.grid(row=3,column=1,padx=10,pady=5)
Bb=Button(F3,text="←",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,command=bckspc,font=('Sans',10,'bold'))#backspace
Bb.grid(row=3,column=2,padx=10,pady=5)
F3.configure(bg="#152238")
#Entry
F4=LabelFrame(a)
F4.grid(row=2,column=5,pady=5)
e=Entry(F4,width=40)#Entry box
e.pack()
#mainframe
mainframe=LabelFrame(a)
mainframe.grid(row=0,column=5)
label=Label(mainframe,bg="#ADD8E6",width=50,height=25)
label.grid(row=0,column=0)
lbm=Label(mainframe,text="Enter your account number:",width=50,height=25,bg="black",fg="white").grid(row=0,column=0)#Account_Number*
Belbm=Button(F3,text="Enter ",fg="black",bg="#808080",padx=10,pady=10,width=5,relief=RIDGE,font=('Sans',10,'bold'),command=elbm)#enter
Belbm.grid(row=3,column=0,padx=10,pady=5)



mainframe.config(bg="blue")
a.config(bg="#00008B")
a.mainloop()
