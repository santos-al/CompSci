from um import count

def test_more_than_one():
    assert count("Um, thanks, um...") == 2
    assert count("cat") == 0

def test_one():
    assert count("Um, thanks") == 1
    assert count("um") == 1
    assert count("album") == 0
