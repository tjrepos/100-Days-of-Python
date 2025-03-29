#A classic game of Rock, Paper, Scissors
import random

def spr():
    options = ["Rock", "Paper", "Scissors"]
    computer_option = random.choice(options)
    player_choice = int(input("""Please choose
    1 - Rock
    2 - Paper
    3 - Scissors
    Enter your choice: """))
    player_choice = player_choice - 1
    if player_choice < 0 or player_choice > 2 :
        print("Invalid option. Please try again.")
        player_choice = 0
        spr()
    elif player_choice > 0 or player_choice < 3:
        player_option = options[player_choice]
        print(f"Computer: {computer_option}")
        print(f"Player: {player_option}")
        if computer_option == player_option:
            print("It's a tie!!")
        elif (computer_option == options[0] and player_option == options[2]) or (computer_option == options[2] and player_option == options[0]):
            print(f"{options[0]} breaks {options[2]}!!")
            if computer_option == options[0]:
                print("Computer wins!!!")
            else:
                print("You win!!")
        elif (computer_option == options[1] and player_option == options[0]) or (computer_option == options[0] and player_option == options[1]):
            print(f"{options[1]} covers {options[0]}!!")
            if computer_option == options[1]:
                print("Computer wins!!!")
            else:
                print("You win!!")
        elif (computer_option == options[2] and player_option == options[1]) or (computer_option == options[1] and player_option == options[2]):
            print(f"{options[2]} cuts {options[1]}!!")
            if computer_option == options[2]:
                print("Computer wins!!!")
            else:
                print("You win!!")
        again = input("Play again? Y/N: ")
        match again:
            case "Y":
                spr()
            case _:
                print("Quitting the game...")
                quit()


spr()