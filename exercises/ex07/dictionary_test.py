"""Test folder for EX07."""

__author__ = "730602160"
# comand to run tests: python -m pytest exercises/ex07
from dictionary import invert, favorite_color, count
import pytest


def test_invert() -> None:
    """General Test."""
    assert invert({'Jay': 'Son', "Bran": "Don", "Ke": "Vin"}) == {"Son": "Jay", "Don": "Bran", "Vin": "Ke"}


def test_invert_2() -> None:
    """Second Invert Test. Only One Pair."""
    assert invert({'Jay': 'Son'}) == {'Son': 'Jay'}


def test_invert_3() -> None:
    """Third Test. Meant To Produce KeyError.""" 
    with pytest.raises(KeyError):
        test_dict = {'Jay': 'Son', 'Bran': 'Son'}
        invert(test_dict)


def test_count() -> None:
    """First Test. Empty List Should Equal Zero."""
    assert count({}) == {}


def test_count2() -> None:
    """Second Test. General Test."""    
    assert count(['Brown', 'Brown', 'Blue', 'Green']) == {'Brown': 2, 'Blue': 1, 'Green': 1}


def test_count3() -> None:
    """Third Test. Empty List."""
    assert count([]) == {}    


def favorite_color_test() -> None:
    """First Test. General Test."""
    assert favorite_color({'Ben': 'Blue', 'Jayson': 'Green', 'Anukul': 'Blue', 'Millie': 'Brown'}) == "Blue"


def favorite_color_test2() -> None:
    """Second Test. Empty List."""
    assert favorite_color({}) == ""


def favorite_color_test3() -> None:
    """Third test. General test."""
    assert favorite_color({'Jay': 'Green', 'Mimo': 'Black', 'Julia': 'Green'}) == "Green"    