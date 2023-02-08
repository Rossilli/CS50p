from numb3rs import validate

def test_ip_true():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

def test_ip_false():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("255.255.") == False
    assert validate("111") == False
