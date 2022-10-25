"One Shot Wordle - 09/07/2022"

__author__= "730602160"

secret: str = ("python")
secret_length: int = len(secret)
guess: str = input(f"What is your {secret_length}-letter guess? ")
i: int = 0
guess_result: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001FA99"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(secret):
    guess = input(f"That was not {secret_length}-letters! Try again: ")

while i < len(secret):
    
    if guess[i] == secret[i]:
       guess_result = guess_result + GREEN_BOX

    else: 
        present: bool = False
        alternate: int = 0
        while not present and alternate < len(secret):
            if guess[i] == secret[alternate]:
                present = True

            else: 
                alternate = alternate + 1

        if present == True:
            guess_result = guess_result + YELLOW_BOX
        else:
            guess_result = guess_result + WHITE_BOX
    
    i = i + 1
print(guess_result)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

    


 

