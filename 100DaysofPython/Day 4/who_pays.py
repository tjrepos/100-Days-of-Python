#Figure out who pays the bill
import random
friends = ["Bill", "Ted", "Jane", "Sally", "Monique", "Manuel"]

def who_pays():
    payer = random.choice(friends)
    print(f"Congratulations {payer}!!! It's your turn to pay the bill!!")
    who_pays_menu = input("""Would you like to play again?
    1 - Yes
    2 - Return to Main Menu
    3 - Quit
    Please enter your choice: """)
    who_pays_menu = int(who_pays_menu)
    match who_pays_menu:
        case 1:
            who_pays()
        case 2:
            print("Returning to main menu...")
            main()
        case 3:
            print("Thank you for playing the Who Pays Game!!! Exiting...")
            quit()
        case _:
            print("Error. Invalid Input. The game will now return to the main menu.")
            main()


def new_friend():
    friends.append(input("Please enter the name of the new friend to add to the game: " ))
    new_friend_menu = input("""Would you like add another friend to the list? 
    1 - Yes
    2 - Play the game
    3 - Return to main menu
    Please enter your choice: """)
    new_friend_menu = int(new_friend_menu)
    if new_friend_menu == 1:
        new_friend()
    elif new_friend_menu == 2:
        who_pays()
    elif new_friend_menu ==3:
        main()

def main():
    main_menu = input("""Welcome to the Who Pays Game
    1 - See who pays
    2 - Add a new friend to the game
    3 - Exit the game
    Please enter your choice: """)
    main_menu = int(main_menu)
    match main_menu:
        case 1:
            who_pays()
        case 2:
            new_friend()
        case 3:
            print("The game will now exit.")
            quit()
        case _:
            print("Invalid input. Please try again!!")
            main()


main()