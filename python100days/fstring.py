age = input("What is your current age? ")

int_age = int(age)

years_left = 90 - int_age 
days = years_left * 365
weeks = years_left * 52
months = years_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")


