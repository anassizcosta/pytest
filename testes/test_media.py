from calculadora import calcular_media

def test_1():
    assert calcular_media(7,8,9) == 8

def test_2():
    assert calcular_media(0,0,0) == 0

def test_3():
    assert calcular_media(5,6,7) == 6
