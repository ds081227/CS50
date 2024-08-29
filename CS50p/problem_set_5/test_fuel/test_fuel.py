import pytest
from fuel import convert, gauge
def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
def test_gauge_E():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
def test_gauge_percentage():
    assert gauge(25) == "25%"
def test_letters():
    with pytest.raises(ValueError):
        convert("a/b")
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
