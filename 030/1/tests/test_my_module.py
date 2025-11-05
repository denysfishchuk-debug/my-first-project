import pytest
from src.my_module import add, is_even, return_true

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True

def test_return_true():
    assert return_true() is True
