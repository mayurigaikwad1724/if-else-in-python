a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if a>b and a>c:
    print("Max number is 1st number=",a)
elif b>a and b>c:
    print("Max number is 2nd number=",b)
else:
    print("Max number is 3rd number=",c)        