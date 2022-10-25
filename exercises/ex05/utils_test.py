"""Second file in ex05."""

__author__ = "730602160"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Tests only evens."""
    sample: list[int] = [1, 2, 3, 4]
    assert only_evens(sample) == [2, 4]


def test_only_evens2() -> None:
    """Second evens Test."""
    sample: list[int] = [1, 2, 3, 6]
    assert only_evens(sample) == [2, 6]


def test_only_evens3() -> None:
    """Third evens Test."""
    sample: list[int] = []
    assert only_evens(sample) == []


def test_concat() -> None:
    """Tests concat."""
    l_one: list[int] = [1, 2, 3, 4]
    l_two: list[int] = [1, 2, 3, 4]
    assert concat(l_one, l_two) == [1, 2, 3, 4, 1, 2, 3, 4]


def test_concat2() -> None:
    """Tests concat."""
    l_one: list[int] = [1, 2, 5]
    l_two: list[int] = [1, 2, 3, 4]
    assert concat(l_one, l_two) == [1, 2, 5, 1, 2, 3, 4]


def test_concat3() -> None:
    """Tests concat."""
    l_one: list[int] = []
    l_two: list[int] = []
    assert concat(l_one, l_two) == []


def test_sub() -> None:
    """Tests sub."""
    sample: list[int] = [1, 2, 3, 4]
    begin: int = 1
    finish: int = 3
    assert sub(sample, begin, finish) == [2, 3]


def test_sub2() -> None:
    """Tests sub."""
    sample: list[int] = [1, 2, 3, 4, 5]
    begin: int = 1
    finish: int = 4
    assert sub(sample, begin, finish) == [2, 3, 4]


def test_sub3() -> None:
    """Tests sub."""
    sample: list[int] = []
    begin: int = 0
    finish: int = 0
    assert sub(sample, begin, finish) == []        
