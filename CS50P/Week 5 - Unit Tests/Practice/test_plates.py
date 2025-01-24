"""
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, 
wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it 
does not, but main is only called if the value of __name__ is "__main__":

def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()
    
Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of 
is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
"""

from plates import is_valid

def test_alpha_start():
    assert is_valid("2A") == False
    assert is_valid("AA") == True
    assert is_valid("22") == False
    assert is_valid(" 1") == False
    assert is_valid("A2") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("ABC") == True

def test_num_placement():
    assert is_valid("ABC1A") == False
    assert is_valid("ABC1") == True

def test_zero_placement():
    assert is_valid("ABC0") == False
    assert is_valid("ABC10") == True

def test_alpa_num():
    assert is_valid("ABC!") == False
    assert is_valid("ABC") == True


