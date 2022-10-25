
def zip(a:list[str], b:list[str]) -> dict[str,str]:
    """Takes two lists and returns a combination of both as a dictionary."""
    assert len(a) == len(b)
    comebine: dict[str, str] = {}
    i: int = 0
    while i < len(a):
        comebine[a[i]] = b[i]
        i += 1
    return comebine


print(zip(["Hey", "Wow", "Ok"], ["No", "Now", "Bye", "Cow"]))        
