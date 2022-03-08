
x=int(input("Enter the age:-"))
if(x>=5):
    print("You can go to school")
    if(x>=18):
        print("You can vote in elections")
        if(x>=21):
            print("You can drive a car and a motarbike")
            if(x>=24):
                print("You can marry")
                if(x>=25):
                    print("You can legally drink")
                else:
                    print("You can noy legally drink")
            else:
                print("You can not marry")
        else:
            print("You can not drive a car and a motarbike")
    else:
        print("You can not vote in elections")
else:
    print("You can not go to school")      