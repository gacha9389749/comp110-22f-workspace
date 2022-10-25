"""Excersize 5, due wednesday."""

__author__ = "730602160"


def only_evens(sample: list[int]) -> int:
    """Returns even values."""
    i: int = 0
    new_list: list[int] = list()
    while i < len(sample):
        if sample[i] % 2 == 0:
            new_list.append(sample[i])
            i += 1
        else:
            i += 1
    return new_list        


def concat(l_one: list[int], l_two: list[int]) -> int:
    """Returns two lists put together."""
    i: int = 0
    final_list: list[int] = list()   
    while i < len(l_two):
        final_list.append(l_two[i])
        i += 1
    i = 0
    while i < len(l_one):
        final_list.append(l_one[i])
        i += 1  
    return final_list 


def sub(sample: list[int], begin: int, finish: int) -> int:
    """Returns requested section of list."""
    i: int = begin
    new_list: list[int] = list()
    if i < 0:
        i = 0
    if finish > len(sample):
        finish = len(sample)
    while i < finish:
        new_list.append(sample[i])
        i += 1
    return new_list    