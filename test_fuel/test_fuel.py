from fuel import convert, gauge
import pytest

def main():
    test_input()
    test_zerodiv()

def test_input():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

def test_zerodiv():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_valueerror():
    with pytest.raises(ValueError):
        convert("doggy/mouse")
if __name__ == "__main_":
    main()