from aprovacao import verificar_aprovacao

def test_1():
    assert verificar_aprovacao(7) == "Aprovado"

def test_2():
    assert verificar_aprovacao(6) == "Recuperação"

def test_3():
    assert verificar_aprovacao(4.9) == "Reprovado"
