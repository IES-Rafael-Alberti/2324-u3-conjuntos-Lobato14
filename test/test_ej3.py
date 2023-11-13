from src.Ejercicio_3 import conjunto_potencia

def test_conjunto_potencia():
    assert conjunto_potencia({}) == [set()]
    assert conjunto_potencia({1}) == [set(), {1}]
    assert conjunto_potencia({1, 2}) == [set(), {1}, {2}, {1, 2}]
    assert conjunto_potencia({1, 2, 3}) == [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]