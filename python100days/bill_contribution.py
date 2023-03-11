bill_amount = float(input("What was total bill? "))
no_of_people = int(input("Enter total number of people here: "))
tip_percentage = float(input("What percentage tip you would like to give? 10,12 or 15? "))
bill_contribution = float(bill_amount / no_of_people)
tip =  bill_amount * tip_percentage / 100
total_contribution = round(bill_contribution + tip , 2)
print(f"Your total contribution is {total_contribution} ")




