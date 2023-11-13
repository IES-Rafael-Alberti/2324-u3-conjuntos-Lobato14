from src.Ejercicio_6 import encontrar_consonantes, obtener_palabra_valida, encontrar_letras_comunes

def test_encontrar_consonantes():
    assert encontrar_consonantes() == {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}

def test_obtener_palabra_valida(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    assert obtener_palabra_valida() == 'abc'

def test_encontrar_letras_comunes():
    consonantes = encontrar_consonantes()
    vocales = {'a', 'e', 'i', 'o', 'u'}
    letras_palabra, letras_consonantes = encontrar_letras_comunes('example', consonantes, vocales)
    assert letras_palabra == {'a', 'e', 'l', 'm', 'p', 'x'}
    assert letras_consonantes == {'l', 'm', 'p', 'x'}