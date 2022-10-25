"""Exercises 4, 9/19."""

__author__ = "730602160"


"""Used to find if whole int is the same as singular int."""


def all(selection: list[int], compare: int) -> bool:
    """Used to find if whole int is the same as singular int."""
    i: int = 0
    if len(selection) != 0:
        while i < len(selection):
            if selection[i] == compare:
                i += 1
            else:
                return False
        return True
    else:
        return False


"""Used to find max value in a list."""        


def max(input: list[int]) -> int:
    """Used to find max value in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    maximum: int = -100
    i: int = 0
    while i < len(input):
        if input[i] >= maximum:
            maximum = input[i]
            i += 1
        else:
            i += 1
    return maximum           


"""Compares two lists to see if they are equal."""


def is_equal(l_one: list[int], l_two: list[int]) -> bool:
    """Compares two lists to see if they are equal."""
    i: int = 0
    if len(l_one) == len(l_two):
        while i < len(l_one):
            if l_one[i] == l_two[i]:
                i += 1
            else:
                return False
        return True                    
    else:
        return False        