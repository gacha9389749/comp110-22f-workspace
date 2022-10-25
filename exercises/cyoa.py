"""Choose your own adventure."""

__author__ = "730602160"

import random

points: int = 0
player: str = ""
path: int = 0
COIN: str = "\U0001FA99"
CAT: str = "\U0001F408"
DOG: str = "\U0001F415"
BIRD: str = "\U0001F426"


def main() -> None:
    """Start button."""
    greet()
    menu()
    play()


def greet() -> None:
    """Greet the user."""
    global player
    player += input("Greetings! Ready to set off on your journey? What is your name? ")
    print(f"Alright {player}, Nice to meet you!")


def cash_in_dog(cost: int = 8) -> int:
    """Custom Function to change variable player and update points variable."""
    global player
    global points
    player += DOG
    print(f"Here is your dog {player}!")
    points = points - cost
    return points


def cash_in_cat(cost: int = 10) -> int:
    """Custom Function to change variable player and update points variable."""
    global player
    global points
    player += CAT
    print(f"Here is your cat {player}!")
    points = points - cost
    return points


def cash_in_bird(cost: int = 2) -> int:
    """Custom Function to change variable player and update points variable."""
    global player
    global points
    player += BIRD
    print(f"Here is your bird {player}!")
    points = points - cost
    return points


def shop() -> None:
    """Takes interger and uses a custom function to change player variable."""
    global player
    global points
    selection: int = int(input("Want a pet? for a Dog (8 points), type '1'. For a Cat (10 points), type '2'. For a bird (2 points), type '3'. To return to the menu, type '4'."))
    while selection != 1 and selection != 2 and selection != 3 and selection != 4 and selection != int:
        selection = int(input("That was not an option. Please choose '1', '2' or '3'."))
    if selection == 1:
        if points >= 8:
            cash_in_dog(8)
            menu()
        else:
            print("You cannot afford that! Leave my shop now.")
            menu()
    
    elif selection == 2:
        if points >= 10:
            cash_in_cat(10)
            menu()
        else:
            print("You cannot afford that! Leave my shop now.")
            menu()
    
    elif selection == 3:
        if points >= 2:
            cash_in_bird(2)
            menu()
        else:
            print("You cannot afford that! Leave my shop now.")
            menu()

    elif selection == 4:
        menu()                


def menu() -> None:
    """Four pathways."""
    global path
    global player
    path = int(input(f"For instructions type '1'! Ready to play, {player}? Type '2'! Want to quit and see your score? Type '3'! Want to access the shop? Type '4'!"))
    while path != 1 and path != 2 and path != 3 and path != 4 and path != int:
        path = int(input("That was not an option. Please choose '1', '2' or '3'."))
    if path == 1:
        instructions()
    elif path == 2:
        play()
    elif path == 3:
        finish() 
    elif path == 4:
        shop()       


def reset_points() -> None:
    """Resets point tally."""
    global points
    points = 0
    print(f"Points reset. Currently at {points} points.")
    menu()


def instructions() -> None:
    """Show character how to play."""
    print(f"Guess which side the coin {COIN}   will fall on when flipped. Every time you guess right, you get a point! Collect pets as you succeed!")
    menu()


def play() -> None:
    """Takes an int and ultimately updates the points value."""
    global points
    r1: int = random.randint(1, 2)
    choice: int = int(input(f"Coin Flip! {COIN} For heads, choose 1. For Tails, choose 2."))
    while choice != 1 and choice != 2 and choice != int:
        choice = int(input("That was not an option. Please choosoe 1 or 2."))    
    if r1 == choice:
        points += 1
        print(f"Got it! Sitting at {points} point(s)!")
        play_again()
    else:
        print(f"Unlucky! You got it wrong. Sitting at {points} point(s).")
        play_again()    


def play_again() -> None:
    """Game loop."""
    global points
    again: int = int(input("Would you like to play again? Press '1'. Want to exit and see your score? Press '2'. Want to rest your score and play again? Type '3'."))
    while again != 1 and again != 2 and again != 3 and again != int:
        again = int(input("That was not an option. To play again, type '1'. To exit and see your score, press '2'. To reset your score and play again, Type '3'."))   
    if again == 1:
        play()
    elif again == 2:
        finish()    
    elif again == 3:
        points = 0
        print(f"Points reset. Currently at {points} points.")
        play()


def finish() -> None:
    """Options for main menu or quit."""
    global points
    global player
    fin: int = int(input(f"Well, that's a wrap! You've finished with {points} points. If you'd like to return to main menu, type '1'. If you'd like to quit, press'2'."))
    while fin != 1 and fin != 2 and fin != int:
        fin = int(input(f"That was not an option {player}. Please choose '1' or '2'."))
    if fin == 1:
        menu()
    elif fin == 2:
        print(f"Thanks for playing {player}!. You have finished with {points} point(s). See you next time!")
        quit()            


if __name__ == "__main__":
    main()