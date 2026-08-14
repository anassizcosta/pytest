from contagemregressiva import contagem_regressiva

def test_1():
    assert contagem_regressiva(5) == [5,4,3,2,1,0]

def test_2():
    assert contagem_regressiva(3) == [3,2,1,0]

def test_3():
    assert contagem_regressiva(0) == [0]
