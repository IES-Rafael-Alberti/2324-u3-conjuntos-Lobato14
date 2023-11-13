from src.Ejercicio_2 import mostrar_alumnos, mostrar_nombres_repetidos, mostrar_nomb_primaria_no_sec, verificar_nomb_primaria_sec

def test_mostrar_alumnos():
    nombres_primaria = ["Juan", "María", "Pedro"]
    nombres_secundaria = ["Pedro", "Elena", "Juan", "Carlos"]
    assert mostrar_alumnos(nombres_primaria, nombres_secundaria) == (["Juan", "María", "Pedro"], ["Carlos", "Elena", "Juan", "Pedro"])

def test_nombres_repetidos():
    nombres_primaria = ["Juan", "María", "Pedro"]
    nombres_secundaria = ["Pedro", "Elena", "Juan", "Carlos"]
    # Ordenar las listas antes de la comparación
    assert sorted(mostrar_nombres_repetidos(nombres_primaria, nombres_secundaria)) == ["Juan", "Pedro"]


def test_nombres_no_rep_sec():
    nombres_primaria = ["Juan", "María", "Pedro"]
    nombres_secundaria = ["Pedro", "Elena", "Juan", "Carlos"]
    assert mostrar_nomb_primaria_no_sec(nombres_primaria, nombres_secundaria) == ["María"]

def test_inclusion_primaria_secundaria():
    nombres_primaria = ["Juan", "María", "Pedro"]
    nombres_secundaria = ["Pedro", "Elena", "Juan", "Carlos"]
    assert verificar_nomb_primaria_sec(nombres_primaria, nombres_secundaria) == False