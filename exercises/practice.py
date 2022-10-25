def my_max(a: int, b: int) -> int:
    if a>=b: return a

    else:
        return b


    i: int = 1
    turns: str = f"=== Turn {i}/6 ==="
    win: bool = False
    secret_word: str = 'codes'
    guess = input_guess(5)
    while i <= 6 and win == False:
        print(turns)
        
        if guess == secret_word:
            win = True
            (emojified(input_guess(5), secret_word))
            print(f"You won in {i}/6 turns!")
            quit()

        else:
            i = i + 1
                


    return "X/6 - Sorry, try again tomorrow!"         