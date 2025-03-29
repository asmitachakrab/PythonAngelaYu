print("Welcome to the rollercoaster!")

height = input("What is your height in cm? ")
if height.isdigit():
    height = int(height)
    
    if height >= 120:
        print("You can ride the rollercoaster!")
        
        age = input("What is your age? ")
        if age.isdigit():
            age = int(age)
            if age < 12:
                bill = 5
            elif age <= 18:
                bill = 7
            else:
                bill = 12
            print(f"Please pay ${bill}.")

            print("Do you want photos? Y or N ")
            photo = input().strip().upper()
            if photo == "Y":
                bill += 3

            print(f"Your final bill is ${bill}.")
            print("Enjoy your ride!")

        else:
            print("Invalid age input. Please enter a number.")

    else:
        print("Sorry, you have to grow taller before you can ride.")

else:
    print("Invalid height input. Please enter a number.")
