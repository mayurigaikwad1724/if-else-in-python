print("ATM Program...")
atm_pin=7860
transcation=["withdraw money","balance enquiry"]
swipe=input("swipe your card here:-")
if(swipe=="cheap"):
    print("Welcome to Money World Bank!!")
    language=input("Enter your language:-")
    if(language=="english"or"hindi"or"marathi"):
        account=input("Enter your account:-")
        if(account=="saving"or"current"):
            pin=int(input("Enter your pin to proceed:-"))
            if(pin==7860):
                trans=input("Enter your trancation:-")
                if(trans=="withdraw money"):
                    amount=int(input("Enter your amount to proceed:-"))
                    if(amount>0):
                        print("collect your case, thanks for using Money World Bank.")
                    else:
                        print("please enter valid amount to proceed.")    
                elif(trans=="balance enquiry"):
                    sleip=input("Do you want sliep ?")
                    if(sleip=="yes"):
                        print("here is your sliep! thanks for using Money World Bank.")
                    else:
                        print("please come again! thanks for using Money World Bank.")
                else:
                    print("choose valid transcation to proceed.")
            else:
                print("wrong pin! please enter valid pin to preoceed.")
        else:
            print("choose valid account to proceed.")
    else:
        print("please choose valid language to proceed.")
else:
    print("swipe your card correctly.")   