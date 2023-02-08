from plates import is_valid

def main():
    test_charmax()
    test_starts_with_two()
    test_middle_numb()
    test_zero()

def test_charmax():
    assert is_valid("A") == False
    assert is_valid("ABCDEF") == True
    assert is_valid("ONED") == True
    assert is_valid("HSKHFKFKH") == False

def test_starts_with_two():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False

def test_middle_numb():
    assert is_valid("AAA111") == True
    assert is_valid("AAA22A") == False

def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_punc():
    assert is_valid("PI3.14") == False


if __name__ == "__main__":
    main()