a=int(input("Enter the physics number="))
b=int(input("Enter the chemistry number="))
c=int(input("Enter the mathematics number="))
d=int(input("Enter the biology number"))
e=int(input("Enterthe computer number="))
total=a+b+c+d+e
percentage=(total/500)*100
print("Total Marks=",total,"Percentage=",percentage,)
if(percentage>=90):
    print("You have got Grade A")
elif(percentage>=80):
    print("You have got Grade B")
elif(percentage>=70):
    print("You have got Grade C")
elif(percentage>=60):
    print("You have got Grade D")
elif(percentage>=40):
    print("You have got Grade E")
else:
    print("You have got Grade F") 