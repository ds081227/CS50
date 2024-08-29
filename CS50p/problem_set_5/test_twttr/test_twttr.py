from twttr import shorten

def test_vowels():
    assert shorten("twitter") == "twttr"
def test_novowel():
    assert shorten("CS50") == "CS50"
def test_punctuation():
    assert shorten(";;!!") == ";;!!"
def test_capital():
    assert shorten("TWITTER") == "TWTTR"

