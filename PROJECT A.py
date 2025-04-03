print("        "*20,"Welcome to ATM")
balance=200000
pin=1431
c=input("Insert your card:")
if("card"==c.lower()):
    num=int(input("Enter any number between 10 and 99:"))
    if(10<num<99):
        Pin=int(input("Enter your 4-digit pin:"))
        if(Pin==pin):
            select=input("Select \' Balance Enquiry \' or  \'Withdrawal\':")
            if("balance enquiry"==select.lower()):
                print("Your balance is",balance,"/-")
                print("Thank you \n Visit again...")
            elif("withdrawal"==select.lower()):
                select1=input("Select \'KCC\' or\'Current \' or \' Savings \' :")
                select1=select1.lower()
                if(select1=="kcc"or select1=="current"or select1=="savings"):
                    money=int(input("How much money you want to credit:"))
                    if(money>100 and money%100==0 and money<balance):
                        print(money,"/- is credited.\n Transaction succeded\n Thank you. \n Visit again.")
                    else:
                        if(money>balance):
                            print("Insufficient funds \n Transaction cancelled. \n Try again...")
                        else:
                            print("Given money is not valid. \n Transaction cancelled. \n Try again...")
                else:
                    print("Not valid. \n Transaction cancelled. \n Try again...")
            else:
                print("Not valid.\n Transaction cancelled. \n Try again...")
        else:
            print("Incorrect pin...\n Transaction cancelled.  \n Try again...")
    else:
        print("Number should be between 10 and 99 only.\n Transaction cancelled. \n Try again...")
else:
    print("Invalid attempt. \n Transaction cancelled \n Try again.")

                        
                        
                
