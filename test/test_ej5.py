from src.Ejercicio_5 import conjunto_pares, multiplos_tres, intersecion_pares_multiplos

def test_conjunto_pares():
    assert conjunto_pares({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) == {2, 4, 6, 8, 10}

def test_multiplos_tres():
    assert multiplos_tres({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) == {3, 6, 9}

def test_intersecion_pares_multiplos():
    assert intersecion_pares_multiplos({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) == {6}