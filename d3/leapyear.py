year = int(input("Which year do you want to check? "))
👇

if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print("Leap Year.")

if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 != 0 :
            print("Not Leap Year.")

if year % 4 == 0 :
    if year % 100 != 0 :
            print("Leap Year.")

if year % 4 != 0 :
    print("Not leap year.")



