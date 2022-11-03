#### PROJECT TIP CALCULATOR ###
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
qty_people = int(input("How many people to split the bill? "))

tip_value = total_bill * (percentage_tip/100)

total_pay = round((total_bill + tip_value) / qty_people,2)

print(f"Each person should pay: ${total_pay}")