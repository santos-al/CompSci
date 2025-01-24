from seasons import age_calc
import pytest


# def test_format():
#     with pytest.raises(SystemExit):
#         age_calc("cat")
#     assert age_calc("2000-07-06") == "Twelve million, eight hundred forty-three thousand, four hundred twenty minutes"

# def test_with_words():
#     with pytest.raises(SystemExit):
#         age_calc("January 1, 2005")
#     assert age_calc("2010-07-06") == "Seven million, five hundred eighty-four thousand, five hundred forty minutes"

def test_invalid_year():
    with pytest.raises(SystemExit):
        age_calc("20-08-32")

def test_invalid_everything():
    with pytest.raises(SystemExit):
        age_calc("200-18-32")

def test_future_date():
    with pytest.raises(SystemExit):
        age_calc("3005-07-06")

def test_invalid_month():
    with pytest.raises(SystemExit):
        age_calc("2000-31-31")
def test_invalid_day():
    with pytest.raises(SystemExit):
        age_calc("2000-08-32")
