"""Choose your own adventure."""

__author__ = "730602160"

points: int = 0
player: str = ""
path: int = 0
hp: int = 100
dog: str = "\U0001F436"
cat: str = "\U0001F431"
bird: str = "\U0001F426"

def main() -> None:
    """Start button."""
    greet()
    menu()



        
def greet() -> None:
    """Greet the user."""
    global player
    player += input("Greetings! Ready to set off on your journey? What is your name? ")
    print(f"Alright {player}, Nice to meet you!")
 
def menu() -> None:
    "Three pathways."
    global path
    path = int(input(f"For instructions type '1'! Ready to play, {player}? Type '2'! Want to quit and see your score? Type '3'! "))
    if path == 1:
        instructions()
    elif path == 2:
        play()
    elif path == 3:
        finish()    

def instructions() -> None:
    "Show character how to play."
    print("Embark on a journey! Try to survive, make a choice out of the selections presented! When your hp drops to zero, game over!")
    proceed: int = input("Return to menu? Enter any character.")
    if 1 == 1:
        menu()

def play() -> None:
    """Game starts."""
    
    stage_1: int = int(input("You wake up in a room. You need to escape. There is a window, a trap door and a regular door. To exit through the window, type '1'. To exit through the trapdoor, type '2'. To exit through the regular door type '3'."))
    global hp
    global points
    while stage_1 != 1 and stage_1 != 2 and stage_1 != 3:
        stage_1 = int(input("That was not an option; type 1, 2 or 3."))
    if stage_1 == 1:
        hp = 0
        print(f"The room was 3 stories up. You fell on to concrete and met your demise. Points: {points}")
        finish()
    elif stage_1 == 2:
        hp = 75
        points += 100
        print(f"You fall into a hallway on the floor beneath you. You taken 25 hp damage but you survive! Points: {points}")
        outcome: int = int(input("You continue down a set of stairs and see a front door and a back door. An old man is sitting by the front door. The back door is free. Type '1' to go through the front door, or type '2' to go through the back door."))
        while outcome != 1 and outcome != 2:
            ouctome = int(input("That was not an option; type 1, or type 2."))
        if outcome == 1:
            outcome_2: int = int(input(f"You walk to the old man in front of the door. 'Greg is that you?' Are you Greg? Type '1'. Are you {player}? Type '2'."))
            while outcome_2 != 1 and outcome_2 != 2:
                ouctome = int(input("That was not an option; type 1, or type 2."))
            if outcome_2 == 1:
                points += 100
                print(f"'Greg! You're late for school! Lets get you on your way.' The old man leads you out the house. You are free! Points: {points}")
                finish()
            elif outcome_2 == 2:
                print(f"What have you done with Greg....The last thing you see is the old man reaching inside his jacket before you black out.")
                finish()    
        elif outcome == 2:
            print("You bolt for the back door before the man can see you. You turn around and close the door. You turn back around to see 3 dobermans waiting for you. There is no way out.")
            finish()
    elif stage_1 == 3:
        points += 100
        outcome_2: int = int(input(f"You walk through the door. You see a man. 'Greg is that you?' Are you Greg? Type '1'. Are you {player}? Type '2'. "))
        while outcome_2 != 1 and outcome_2 != 2:
                ouctome_2 = int(input("That was not an option; type 1, or type 2."))
        if outcome_2 == 1:
                points += 100
                print(f"'Greg! You're late for school! Lets get you on your way.' The old man leads you out the house. You are free! Points: {points}")
                finish()
        elif outcome_2 == 2:
                print(f"'What have you done with Greg....'The last thing you see is the old man reaching inside his jacket before you black out.")
                finish()
               


def finish() -> None:
    print(f"Well, that's a wrap! You've finished with {points} points. Play again soon!")
    quit()
if __name__ == "__main__":
  main()


