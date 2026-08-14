from calculo import calcular_area

def test_1():
    assert calcular_area(5,4) == 20

def test_2():
    assert calcular_area(10,2) == 20

def test_3():
    assert calcular_area(0,5) == 0
