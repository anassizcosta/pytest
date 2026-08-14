from cadastro import cadastrar_produto


def test_nome():
    resultado = cadastrar_produto("Mouse", 89.90, 15)
    assert "Mouse" in resultado


def test_preco():
    resultado = cadastrar_produto("Teclado", 100, 10)
    assert "R$ 100.00" in resultado


def test_estoque():
    resultado = cadastrar_produto("Monitor", 500, 8)
    assert "8 unidades" in resultado