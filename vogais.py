def contar_vogais(texto):
    return sum(1 for letra in texto.lower() if letra in "aeiou")
