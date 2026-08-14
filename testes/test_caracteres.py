from caracteres import contar_caracteres

def test_1():
    assert contar_caracteres("Python") == 6

def test_2():
    assert contar_caracteres("") == 0

def test_3():
    assert contar_caracteres("Olá mundo") == 9
