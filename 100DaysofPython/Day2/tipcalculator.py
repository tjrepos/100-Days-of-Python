
#Tip calculator script

print("""Welcome to the tip calculator!

This script will calculate the amount each individual has to pay including tip
""")

bill_total = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage would you like to tip? "))
number_payees = int(input("How many people are splitting the bill? "))


tip_amount = bill_total * (tip_percent / 100)
check_total = bill_total + tip_amount
individual_total = round(check_total / number_payees, 2)
individual_bill = round (bill_total /  number_payees, 2)
individual_tip = round(tip_amount / number_payees, 2)

print(f"""
Each person should pay ${individual_total}. 

Each person pays ${individual_bill} for the bill and ${individual_tip} for the tip.
""")
