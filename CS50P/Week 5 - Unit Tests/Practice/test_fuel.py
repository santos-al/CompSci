"""
Refueling
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded 
to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a 
ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
def main():
    ...


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()
    
Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert 
and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
"""

from fuel import convert
from fuel import gauge
import pytest


def test_convert():
    assert convert("9/10") == 90
    with pytest.raises(ValueError):
        convert("1/Y")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_guage():
    assert gauge(90) == "90%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
