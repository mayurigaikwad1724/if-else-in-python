age=int(input("Enter the age:-"))
sex=str(input("Enter the sex:-"))
marry=str(input("Enter the married status:-"))
if(sex=="F"):
    if(marry=="yes"):
        if(age>=20 and age<=60):
            print("Urban areas only")
        else:
            print("ERROR")
    elif(marry=="no"):
        if(age>=20 and age<=60):
            print("Urban areas only") 
        else:
            print("ERROR")
    else:
        print("ERROR")
elif(sex=="M"):
    if(marry=="yes"):
        if(age>=20 and age<=40):
            print("You can work anywhere")
        elif(age>40 and age<=60):
            print("Urban areas only")
        else:
            print("ERROR") 
    elif(marry=="no"):
        if(age>=20 and age<=40):
            print("You can work anywhere")
        elif(age>40 and age<=60):
            print("Urban areas only")
        else:
            print("ERROR") 
    else:
        print("ERROR")
else:
    print("ERROR")     