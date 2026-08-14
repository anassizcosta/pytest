from pareimpar import eh_par

def test_1():
    assert eh_par(10) == True

def test_2():
    assert eh_par(7) == False

def test_3():
    assert eh_par(0) == True
