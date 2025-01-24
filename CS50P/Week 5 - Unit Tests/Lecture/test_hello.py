from hello import hello

def test_default():
    assert hello() == "Hello, World"

def test_argument():
    for name in ["Alex", "Paul", "John"]:
        assert hello(name) == f"Hello, {name}"