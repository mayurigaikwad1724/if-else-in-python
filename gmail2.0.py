gmail = "jagritiverma20@navgurukul.org"
password = "navgurukul"
a = input("Enter the gmail address:-")
if (a==gmail):
    b = input("Enter the password:-")
    if (b==password):
        print("Welcome",gmail)
    else:
        print("Invalid password, please enter valid password to proceed.")
else:
    print("Invalid gmail address, please enter valid gmail address.")            