from twttr import shorten

def test_shorten():
    assert shorten("Hello") == "Hll"

def test_caps():
    assert shorten("YELLOW") == "YLLW"

def test_num():
    assert shorten("129Joker.") == "129Jkr."