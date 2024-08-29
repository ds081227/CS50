from numb3rs import validate

def test_correct_number():
    assert validate("1.1.1.1") == True
def test_wrong_number():
    assert validate("256.256.256.256") == False
def test_wrong_input():
    assert validate("abc") == False
def test_first_byte():
    assert validate("10.256.256.256") == False

