age=int(input("Enter the age:-"))
sex=str(input("Enter the sex:-"))
if(sex=="F"):
    if(age>=20 and age<=60):
        print("Urban areas only")
    else:
        print("ERROR")
elif(sex=="M"):
    if(age>=20 and age<=40):
        print("You can work anywhere")
    elif(age>40 and age<=60):
        print("Urban areas only")
    else:
        print("ERROR")
else:
    print("ERROR") 