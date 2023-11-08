from src.Ejercicio_6 import encontrar_consonantes, encontrar_letras_comunes

def test_encontrar_consonantes():
    consonantes = encontrar_consonantes()
    assert len(consonantes) == 21

def test_encontrar_letras_comunes():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = encontrar_consonantes()
    letras_comunes = encontrar_letras_comunes(consonantes, vocales)
    assert letras_comunes == set()