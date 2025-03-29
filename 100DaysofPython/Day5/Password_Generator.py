#Password Generator Project
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = []


def add_letters():
    nr_letters = int(input("How many letters would you like in your password?\n"))
    for x in range(nr_letters):
        password_list.append(random.choice(letters))

def add_symbols():
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    for y in range(nr_symbols):
        password_list.append(random.choice(symbols))


def add_numbers():
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    for z in range(nr_numbers):
        password_list.append(random.choice(numbers))


def random_password():
    password_str = "".join(random.sample(password_list, len(password_list)))
    print(f"Your new password is: {password_str}")


def run():
    add_letters()
    add_symbols()
    add_numbers()
    random_password()
    main()


def main():
    print("Welcome to the PyPassword Generator!")
    menu = input("""Press 1 to generate a password
    Press q to quit
    Select an option: """)
    match menu:
        case "1":
            run()
        case "q":
            print("PyPassword Generator will now quit...")
            quit()
        case _:
            print("Invalid input. Please try again...")
            main()


main()