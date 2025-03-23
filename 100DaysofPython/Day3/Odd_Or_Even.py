#Script to check if integer is odd or even

print("""
Welcome to the Odd/Even Checking Script
This script will determine if an integer is odd or even
""")

number = int(input("Please input the integer you wish to check: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")