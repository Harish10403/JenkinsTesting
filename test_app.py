from app import add, subtract

def test_add():
    assert add(3, 5) == 8
    print(3+5)
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    print(10-5)
    assert subtract(0, 5) == -5
