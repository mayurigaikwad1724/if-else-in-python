x=int(input("Enter the first person age:-"))
y= int(input("Enter the second person age:-"))
z=int(input("Enter the third person age:-")) 
if(x>y and x>z):
    print("Oldest is",x)
elif(y>x and y>z):
    print("Oldest is",y)
elif(z>y and z>x):
    print("Oldest is",z)
else:    
    print("All are equal")  