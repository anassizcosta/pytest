from saudacao import saudacao

def test_1():
    assert saudacao("Ana") == "Olá, Ana! Seja bem-vindo."

def test_2():
    assert saudacao("João") == "Olá, João! Seja bem-vindo."

def test_3():
    assert saudacao("") == "Olá, ! Seja bem-vindo."
