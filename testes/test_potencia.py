from potencia import potencia

def test_1():
    assert potencia(2,3) == 8

def test_2():
    assert potencia(5,0) == 1

def test_3():
    assert potencia(0,5) == 0
