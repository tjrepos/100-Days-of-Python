#Pizza Ordering Script

print("""
Welcome! Please enter your pizza order...
""")

size = input("What size pizza would you like? S, M, or L: ")
pepperoni = input("Would you like pepperoni on your pizza? Y/N: ")
extra_cheese = input("Would you like extra cheese? Y/N: ")

bill = 0

if size == "S":
    bill += 15

elif size == "M":
    bill += 20

elif size == "L":
    bill += 25

else:
    print("Invalid pizza size! Please try again!!!")

if pepperoni == "Y":
       if size == "S":
           bill += 2
       else:
           bill += 3

if extra_cheese == "Y":
       bill += 1


print(f"Your order comes to ${bill}. Please tap or insert your card, or insert cash, to pay.")