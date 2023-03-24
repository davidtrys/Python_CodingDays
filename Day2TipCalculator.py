print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? $"))
personCount = int(input("How many people to split the bill? "))

percentTip = int(input("What percentage tip would you like to give (as a whole number)?"))

print(f"Each person should pay ${round(((totalBill*((percentTip/100)+1))/personCount), 2)}")
