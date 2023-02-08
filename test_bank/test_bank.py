from bank import value

def main():
    test_0()
    test_20()
    test_100()
    test_case()


def test_0():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HEllO Chris") == 0

def test_20():
    assert value("howdy") == 20
    assert value("HI") == 20

def test_100():
    assert value("Ayo") == 100
    assert value("What's wrong?") == 100

def test_case():
    assert value("CAPSLOCK") == 100

if __name__ == "__main__":
    main()
