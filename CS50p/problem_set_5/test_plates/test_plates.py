from plates import is_valid

def test_alphaonly():
    assert is_valid("ABCDEF") == True
def test_alphanum():
    assert is_valid("AB1234") == True
def test_starts_with_0():
    assert is_valid("AB0123") == False
def test_maxmin():
    assert is_valid("A") == False
    assert is_valid("1") == False
    assert is_valid("ABC1234") == False
def test_punctuation():
    assert is_valid("ABC!!@") == False
def test_ends_with():
    assert is_valid("AB12B0") == False
def test_startsletter():
    assert is_valid("AB123") == True
    assert is_valid("A123") == False
    assert is_valid("1234") == False
