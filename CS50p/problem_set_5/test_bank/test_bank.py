from bank import value

def test_hello():
    assert value("Hello") == 0

def test_hello_with_words():
    assert value("Hello, Newman") == 0

def test_starts_with_H():
    assert value("How are you") == 20

def test_else():
    assert value("What's happening?") == 100

