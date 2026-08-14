from verificadorsenha import validar_senha

def test_1():
    assert validar_senha("12345678") == "Senha válida"

def test_2():
    assert validar_senha("1234567") == "Senha inválida"

def test_3():
    assert validar_senha("minhasenha123") == "Senha válida"
