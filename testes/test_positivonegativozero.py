from positivonegativozero import classificar_numero

def test_1():
    assert classificar_numero(10) == "Positivo"

def test_2():
    assert classificar_numero(-10) == "Negativo"

def test_3():
    assert classificar_numero(0) == "Zero"
