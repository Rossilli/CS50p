from um import count

def test_partofword():
    assert count("yummy") == 0
    assert count("circumvolution") == 0

def test_nonchar():
    assert count("um ") == 1
    assert count(".um.") == 1

def test_cap():
    assert count("UM") == 1
    assert count("NONUMBER") == 0