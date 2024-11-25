import pytest
from numb3rs import validate

def test_length():
    assert validate("127.0.0") == False
    assert validate("127.0.0.1") == True

def test_large_digits():
    assert validate("512.512.512.512") == False
    assert validate("255.255.255.255") == True
    assert validate("255.255.255.256") == False


def test_word():
    assert validate("Cat") == False
