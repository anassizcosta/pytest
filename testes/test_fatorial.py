from fatorial import fatorial

def test_1():
    assert fatorial(5) == 120

def test_2():
    assert fatorial(0) == 1

def test_3():
    assert fatorial(3) == 6
