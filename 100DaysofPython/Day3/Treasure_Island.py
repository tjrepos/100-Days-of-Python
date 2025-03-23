# Treasure Island Choose Your Own Adventure

def main_menu():
    play_or_quit = input("Would you like to 'play' the game or 'quit'? ")
    if play_or_quit == "play":
        crossroad()
    elif play_or_quit == "quit":
        quit_game()
    else:
        print("Invalid input. Please try again!")
        main_menu()


def quit_game():
    print("Thank you for playing Treasure Island!!! The game will now exit...")
    quit()


def go_again():
    play_again = input("""
            Would you like to play again? Y/N:
            """)
    if play_again == "Y":
        print("""
                Exiting to main menu...""")
        main()
    elif play_again == "N":
        quit_game()
    else:
        print("""
                Invalid input. Please try again!
                """)
        go_again()


def house():
    print("You arrive at the island unharmed. There is a house with three doors")
    which_door = input("Which colour do you choose? 'red', 'yellow' or 'blue'? ")
    if which_door == "yellow":
        print("Congratulations!!! You have found the treasure!!! You are richer than your wildest dreams!!!")
        go_again()
    elif which_door == "red":
        print("""
        As you step into the room beyond the red door, you are consumed by flames!!!

        Please try again!!!""")
        go_again()
    elif which_door == "blue":
        print("""
        As you step into the room beyond the blue door, you are eaten alive by wild beasts!!!

        Please try again!!!""")
        go_again()
    else:
        print("""
        Invalid input. Please try again!
        """)
        house()


def lake():
    print("You've come to a lake. There is an island in the middle.")
    wait_or_swim = input("Would you like to 'wait' for a boat, or 'swim' to the island? ")
    if wait_or_swim == "wait":
        house()
    elif wait_or_swim == "swim":
        print("""
        You are not a strong enough swimmer and you were pulled under the current and drowned. Please try again!
        """)
        go_again()
    else:
        print("""
        Invalid input. Please try again!
        """)
        lake()


def crossroad():
    turn = input("You are at a crossroad. Would you like to go 'left' or 'right'? ")
    if turn == "left":
        lake()
    elif turn == "right":
        print("""
        Oh no! you fell into a hole and died! Please try again!
        """)
        go_again()
    else:
        print("Invalid input. Please try again!")
        crossroad()


def main():
    print('''                                                               
        #####################################################################
        #                                                                   #
        #                  Welcome to Treasure Island!!!                    #
        #                                                                   #
        #             Your Mission is to find the treasure!!!               #
        #                                                                   #            
        #####################################################################
    ''')
    main_menu()


main()
