print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

base_price = 0
if size == "S" :
   base_price += 15
elif size == "M" :
   base_price += 20
else:
   base_price += 25 
if extra_cheese == "Y":
   base_price += 1
if add_pepperoni == "Y":
   if size == "S":
      base_price += 2
   else :
      base_price += 3


print(f"Your final bill is: {base_price}.")
