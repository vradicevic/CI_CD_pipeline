from hello import *

def test_add_one():
    x=10
    assert add_one(x) == 11


def test_subtract_one():
    x=10
    assert subtract_one(x) == 9



if __name__ == "__main__":
    test_add_one()
    test_subtract_one()