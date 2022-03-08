day=str(input("Enter the day name:-"))
meal=str(input("Enter the meal time:-"))
if(day=="monday"):
    if(meal=="breakfast"):
        print("poha")
    elif(meal=="lunch"):
        print("rajama chawal") 
    else:
        print("sabji roti")
elif(day=="tuesday"):
    if(meal=="breakfast"):
        print("puri sabji")
    elif(meal=="lunch"):
        print("dal chawal")
    else:
        print("panner sabji and paratha")
elif(day=="wednesday"):
    if(meal=="breakfast"):
        print("aloo ka paratha and dahi")
    elif(meal=="lunch"):
        print("curry chawal")
    else:
        print("farra chatni")
elif(day=="thursday"):
    if(meal=="breakfast"):
        print("channa ka ghughari")
    elif(meal=="lunch"):
        print("channa ka dal , chawal and roti")   
    else:
        print("sabji roti")
elif(day=="friday"):
    if(meal=="breakfast"):
        print("sandwich")
    elif(meal=="lunch"):
        print("cholaa bhatura")
    else:
        print("veg biryani with curd")
elif(day=="saturday"):
    if(meal=="breakfast"):
        print("upamma")
    elif(meal=="lunch"):
        print("khichdi")
    else:
        print("koptta roti")
elif(day=="sunday"):
    if(meal=="breakfast"):
        print("idli sambhar")
    elif(meal=="lunch"):
        print("rawa dosa sambhar")
    else:
        print("egg curry roti and chawal") 
else:
    print("roti sabji dal and chawal")                                                                                                          
