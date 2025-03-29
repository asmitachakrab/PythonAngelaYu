import sys  # Import sys to exit the program if input is invalid

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n").strip().upper()
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid size. Please restart the order and enter a valid size.")
    sys.exit()
add_pepperoni = input("Do you want pepperoni? Y or N\n").strip().upper()
extra_cheese = input("Do you want extra cheese? Y or N\n").strip().upper()

if add_pepperoni == "Y":
    bill += 2
if extra_cheese == "Y":
    bill += 1

print(f"Your total bill amount is: $ {bill}")
