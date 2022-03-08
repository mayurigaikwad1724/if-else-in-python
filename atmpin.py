print("ATM Program...")
print("Welcome to Money World Bank!!") 
print("Swipe your card here:") 
atm_pin=7860
transcation=["balance enquiry","withdraw money","deposite","change your pin","transfer money","quit"]
pin=int(input("Enter your pin to proceed:-"))
if(pin==7860):
    print("Choose your transcation:")
    print("1. balance enquiry")
    print("2. withdraw money")
    print("3. deposite")
    print("4. change your pin")
    print("5. transfer money")
    print("6. quit")
    trans=str(input("transcation:-"))
    if(trans=="balance enquiry"):
        sleip=str(input("Do you want sleip ?"))
        if(sleip=="yes"):
            print("here is your sleip! thanks for using Money World Bank.")
        else:
            print("thanks for using Money World Bank.")
    elif(trans=="withdraw money"):
        amount=int(input("Enter your amount to proceed:-"))
        if(amount>0):
            print("Collect your case, thanks for using Money World Bank.")
        else:
            print("Enter valid amount to proceed:")
    elif(trans=="deposite"):
        deposite=int(input("Enter your amount to proceed:-"))
        if(deposite>0):
            print("Your deposite has been suceesfully deposited! thanks for using Money World Bank.")
        else:
            print("Enter valid amount to proceed:")
    elif(trans=="change your pin"):
        change_pin=int(input("Enter here your new pin:-"))
        if(change_pin>0):
            print("Your pin has been change suceesfully! thanks for using Money World Bank.")
        else:
            print("Enter valid pin to proceed:")
    elif(trans=="transfer money"):
        transfer_money=int(input("Enter your amount to transfer:-"))
        if(transfer_money>0):
            print("Your amount has been transfered suceesfully! thanks for using Money World Bank.")
        else:
            print("Enter valid amount to proceed:")
    elif(trans=="quit"):
        quit=str(input("Press yes to quit!"))
        if(quit=="yes"):
            print("quit")
        else:
            print("Choose any transcation please.")
    else:
        print("Choose valid transcation please.")
else:
    print("Wrong pin! try again.")     