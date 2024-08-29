from working import convert
import pytest

def test_correct():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
def test_wrong():
    with pytest.raises(ValueError):
        convert("9AM 5PM")
    with pytest.raises(ValueError):
        convert("11:60 AM to 30:90 PM")


