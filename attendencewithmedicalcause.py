x=int(input("Number of classes held:-"))
y=int(input("Number of classes attend:-"))
z=str(input("Medical issues:-"))
atten=(y/float(x))*100
print("Attendence is",atten)
if(atten<75):
    if(z=="yes"):
        print("You are allowed to sit in exam")
    else:
        print("You are not allowed to sit in exam") 
else:
    print("You are allowed to sit in exam")    