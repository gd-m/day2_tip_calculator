print("Welcome to Tip Calculator")
bill = float(input("What was the total bill? \n$"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? \n"))
people = int(input("How many people to split the bill? \n"))    
tip_as_decimal = tip_percentage / 100
total_tip_amount = bill * tip_as_decimal
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
print(f"Each person should pay: ${bill_per_person:.2f}")
