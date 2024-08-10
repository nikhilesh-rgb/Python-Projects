print("Welcome to Tip Calculator!")
bill = float(input("What was the total bill? ₹ "))
tip = int(input("How much tip would you like to give (0-100%)? "))
split = int(input("How many people to split the bill? "))
bill_with_tip = bill * tip/100 + bill
final = str(round(bill_with_tip / split, 2))
print(f"Each person should pay:₹{final}")


