from conversormoedas import converter_dolar

def test_1():
    assert converter_dolar(100,5) == 20

def test_2():
    assert converter_dolar(50,5) == 10

def test_3():
    assert converter_dolar(200,4) == 50
