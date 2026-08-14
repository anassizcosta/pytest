from desconto import calcular_desconto

def test_1():
    assert calcular_desconto(100,10) == 90

def test_2():
    assert calcular_desconto(200,50) == 100

def test_3():
    assert calcular_desconto(100,0) == 100
