from um import count

def test_correct():
    assert count("um") == 1
    assert count("UM?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_unrelated_input():
    assert count("apple") == 0
    assert count("abc123") == 0
def test_wrong_input_with_um():
    assert count("yummy") == 0
    assert count("RUM") == 0

