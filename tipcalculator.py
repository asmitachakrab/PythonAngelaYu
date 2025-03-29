print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
inttip = int(tip)
numpeople = input("How many people to split the bill? ")
intnum = int(numpeople)
totalperhead = (bill + (bill * inttip / 100))/ intnum
print(f"Each person should pay: ${totalperhead:.2f}")