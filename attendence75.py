x=int(input("Number of classes held="))
y=int(input("Number of classes attended="))
z=(y/x)*100
print("Attendence is",z)
if(z>=75):
    print("You are allowed to sit in exam.")
else:
    print("Sorry,you are not allowed.Attend more classes from next time.")    