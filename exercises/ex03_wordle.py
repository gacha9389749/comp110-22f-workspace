"""Wordle Part 3."""

__author__ = "730602160"


def contains_char(guess: str, letter: str) -> bool:
    """Will return true if character is present in index."""
    assert len(letter) == 1   
    i: int = 0
    
    while i < len(guess):
        if guess[i] == letter:
            return True
        i = i + 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Returns string of color coded emoji."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F436"
    YELLOW_BOX: str = "\U0001FA99"
    i: int = 0
    correct: str = ""
    while i < len(secret):
        if secret[i] == guess[i]:
            correct = correct + GREEN_BOX
        elif contains_char(secret, guess[i]):
            correct = correct + YELLOW_BOX
        else:
            correct = correct + WHITE_BOX
        i = i + 1
    return correct            


def input_guess(input_guess: int) -> str:
    """Returns user input if length of string is equal to set index parameter."""
    guessed_len: str = input(f"Enter a {input_guess} character word: ")
    while input_guess != len(guessed_len):
        guessed_len = input(f"That wasn't {input_guess} chars! Try again: ")
    
    return guessed_len    


def main() -> None:
    """Essentially start button."""
    i: int = 1
    win: bool = False
    secret: str = "codes"
    turns: str = f"=== Turn {i}/6 ==="

    while i <= 6 and win is False:
        turns = f"=== Turn {i}/6 ==="
        print(turns)
        response: str = input_guess(len(secret))

        if response == secret:
            print(emojified(response, secret))
            win = True
            print(f"You won in {i}/6 turns!")
            return None

        else:
            print(emojified(response, secret))
        
        i = i + 1
    print("X/6 - Sorry, try again tomorrow!")