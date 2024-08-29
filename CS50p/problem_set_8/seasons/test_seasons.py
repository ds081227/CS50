from seasons import convert
import pytest

def test_correct():
    assert convert("2023-12-27") == 'One thousand, four hundred forty minutes'

def test_wrong_format():
    with pytest.raises(SystemExit):
        convert("27 December 2023")

def test_wrong_input():
    with pytest.raises(SystemExit):
        convert("abc123")
