#Ticket Box Script

print("""
########################################
# Welcome to the Virtual Ticket Box!!! #
########################################

""")

height = int(input("Please enter your height in centimetres: "))

if height >= 120:
    print("Congratulations!! You are tall enough to ride the rollercoaster")
    age = int(input("Please enter your age: "))
    photo = input("Would you like a photo of your ride? Y/N: ")
    bill = 0
    if age <= 12 :
        bill += 5
    elif age < 18:
        bill += 7
    elif 45 <= age <= 55:
        bill = 0
    else:
        bill += 12


    if photo == "Y":
        bill += 3


    if bill > 0:
        print(f"Please insert ${bill} to purchase your ticket...")
    else:
        print("Please enjoy a free ride on us!!!")

else:
    print("Sorry!!! You are not tall enough to ride the rollercoaster.")