from vogais import contar_vogais

def test_1():
    assert contar_vogais("banana") == 3

def test_2():
    assert contar_vogais("AEIOU") == 5

def test_3():
    assert contar_vogais("rhythm") == 0
