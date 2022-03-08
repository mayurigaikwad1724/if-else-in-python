amt=int(input("Enter Sale Amount:-"))
if(amt>0):
    if(amt<=5000):
        disc=amt*0.50
    else:
        if(amt<=15000):
            disc=amt*0.25
        else:
            if(amt<=25000):
                disc=amt*0.20
            else:
                disc=amt*0.10
    print("Discount:-",disc)
    print("Net pay:-",amt-disc)
else:
    print("Invalid Amount")                            