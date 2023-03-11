choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right": ').lower()
if choice1 == "left":
    choice2 = input("swim or wait : ").lower()
    if choice2 == "wait":
        choice3 = input("red, blue, green : ")
        if choice3 == "red":
            print("over")
        elif choice3 == "blue":
            print("won")
        elif choice3 == "green":
            print("over")
        else :
            print("over")
    else:
        print("over")
else:
    print("over")

