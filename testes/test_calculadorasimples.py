from calculadorasimples import somar, subtrair, multiplicar, dividir

def test_1():
    assert somar(5,3) == 8

def test_2():
    assert subtrair(5,3) == 2

def test_3():
    assert multiplicar(5,3) == 15

def test_4():
    assert dividir(10,2) == 5
