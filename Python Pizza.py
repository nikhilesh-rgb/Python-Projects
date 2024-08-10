print("Welcome to Python Pizza Delivery")

bill = 0

size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("The entered size is invalid.")

pepperoni = input("Do you want pepperoni in pizza? Yes or No: ")
if pepperoni == "Yes":
    if size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want extra cheese? Yes or No: ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
