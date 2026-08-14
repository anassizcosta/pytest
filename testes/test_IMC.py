from IMC import calcular_imc

def test_1():
    assert round(calcular_imc(70,1.75),2) == 22.86

def test_2():
    assert round(calcular_imc(50,1.60),2) == 19.53

def test_3():
    assert round(calcular_imc(90,1.80),2) == 27.78
