"""Some tender, loving functions."""

def love(subject: str) -> str:
    "Given a subject as a parameter, returns a loving string"
    return f"I love you {subject}!"


print(love("Jayson"))    


def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note : str = ("")
    c : int = 0

    while c < n:
        love_note += love(to) + "\n"
        c += 1
    return love_note    
