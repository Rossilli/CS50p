from working import convert

def test_TimeConvert():
    assert convert("12:30 am to 1:30 am") == ("00:30 to 01:30")
    assert convert("12:30 PM to 3:30 PM") == ("12:30 to 15:30")

def test_value():
    try:
        assert convert("hello") == ValueError
    except ValueError as e:
        return True
    try:
        assert convert("123 to 890") == ValueError
    except ValueError as e:
        return True

def test_to():
    try:
        assert convert("12:40 am 9:20 pm") == ValueError
    except ValueError as e:
        return True
    assert convert("1:30 pm to 12:30 pm") == "13:30 to 12:30"