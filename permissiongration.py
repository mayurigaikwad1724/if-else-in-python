day=input("Enter day name:-")
if(day=="thursday"):
    per=input("Taken permission from team member:-")
    if(per=="yes"):
        per_2=input("Taken permission from DISCO:-")
        if(per_2=="yes"):
            print("you can go.")
            time=int(input("Time when you reach campus:-"))
            if(time<=7):
                quar=input("Are you vaccinated?")
                if(quar=="yes"):
                    print("you can go into your room.")
                else:
                    print("you have to be quarentine for 3 days.")
            else:
                print("you get a oil for coming late in campus.")
        else:
            print("you can not go.")
    else:
        print("you can not go without team member permission.") 
else:
    print("today is not holiday, in emergency case you have to taken permission from team member then you can go.")                                   
