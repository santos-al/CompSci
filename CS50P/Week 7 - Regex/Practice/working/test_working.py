from working import convert
import pytest

def test_pm_time():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
         convert("9:00 AM to 5:00")

def test_to():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_invalid_time():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("12:60 AM to 3:00 PM")
    with pytest.raises(ValueError):
        convert("12:00 AM to 13:00 PM")
