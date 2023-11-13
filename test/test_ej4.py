from src.Ejercicio_4 import encontrar_frutas_ambos, solo_frutas_1, solo_frutas_2

def test_encontrar_frutas_ambos():
    assert encontrar_frutas_ambos(set({"manzana", "pera"}), set({"manzana", "durazno"})) == {"manzana"}

def test_solo_frutas_1():
    assert solo_frutas_1(set({"manzana", "pera", "naranja"}), set({"naranja", "pera"})) == {"manzana"}

def test_solo_frutas_2():
    assert solo_frutas_2(set({"manzana", "pera", "naranja"}), set({"manzana", "durazno"})) == {"durazno"}