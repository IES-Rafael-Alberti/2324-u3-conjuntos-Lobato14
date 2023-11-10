# Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de 
# una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que 
# introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

# 1. Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
# 2. Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
# 3. Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
# 4. Mostrar si todos los nombres de primaria están incluidos en secundaria.

def mostrar_alumnos(nombres_primaria: list, nombres_secundaria: list) -> tuple:
    """
    Muestra los nombres únicos de los alumnos de primaria y secundaria.

    Parameters
    ----------
    - nombres_primaria : list
        Lista de nombres de alumnos de primaria.
    - nombres_secundaria : list
        Lista de nombres de alumnos de secundaria.

    Returns
    -------
    - tuple
        Tupla que contiene dos listas: nombres únicos de primaria y nombres únicos de secundaria.
    """
    print("\nNombres de todos los alumnos de primaria:")
    nombres_primaria_unicos = sorted(list(set(nombres_primaria)))
    print(nombres_primaria_unicos)
    
    print("\nNombres de todos los alumnos de secundaria:")
    nombres_secundaria_unicos = sorted(list(set(nombres_secundaria)))
    print(nombres_secundaria_unicos)
    return nombres_primaria_unicos, nombres_secundaria_unicos


def mostrar_nombres_repetidos(nombres_primaria_unicos: list, nombres_secundaria_unicos: list) -> list:
    """
    Muestra los nombres que se repiten entre primaria y secundaria.

    Parameters
    ----------
    - nombres_primaria_unicos : list
        Lista de nombres únicos de alumnos de primaria.
    - nombres_secundaria_unicos : list
        Lista de nombres únicos de alumnos de secundaria.

    Returns
    --------
    - list
        Lista de nombres que se repiten entre primaria y secundaria.
    """
    print("\nNombres que se repiten entre primaria y secundaria:")
    nombres_repetidos = list(set(nombres_primaria_unicos) & set(nombres_secundaria_unicos))
    print(nombres_repetidos)
    return nombres_repetidos


def mostrar_nomb_primaria_no_sec(nombres_primaria_unicos: list, nombres_secundaria_unicos: list) -> list:
    """
    Muestra los nombres de primaria que no se repiten en secundaria.

    Parameters
    ----------
    - nombres_primaria_unicos : list
        Lista de nombres únicos de alumnos de primaria.
    - nombres_secundaria_unicos : list
        Lista de nombres únicos de alumnos de secundaria.

    Returns
    -------
    - list
        Lista de nombres de primaria que no se repiten en secundaria.
    """
    print("\nNombres de primaria que no se repiten en secundaria:")
    nombres_no_repetidos = list(set(nombres_primaria_unicos) - set(nombres_secundaria_unicos))
    print(nombres_no_repetidos)
    return nombres_no_repetidos


def verificar_nomb_primaria_sec(nombres_primaria_unicos: list, nombres_secundaria_unicos: list) -> bool:
    """
    Verifica si todos los nombres de primaria están incluidos en secundaria.

    Parameters
    ----------
    - nombres_primaria_unicos : list
        Lista de nombres únicos de alumnos de primaria.
    - nombres_secundaria_unicos : list
        Lista de nombres únicos de alumnos de secundaria.

    Returns
    -------
    - bool
        True si todos los nombres de primaria están incluidos en secundaria, False en caso contrario.
    """
    
    if set(nombres_primaria_unicos).issubset(set(nombres_secundaria_unicos)):
        print("\nTodos los nombres de primaria están incluidos en secundaria.")
        return True
    else:
        print("\nNo todos los nombres de primaria están incluidos en secundaria.")
        return False

if __name__ == "__main__":
    # Entrada
    nombres_primaria = []
    nombres_secundaria = []
    print("Introduce los nombres de los alumnos de primaria (escribe 'x' para terminar):")
    nombre = input("Nombre: ")
    # Proceso
    while nombre.lower() != "x" and (not nombre.isalpha() or len(nombre.strip()) == 0):
        nombres_primaria.append(nombre)
        nombre = input("Nombre: ")

    print("Introduce los nombres de los alumnos de secundaria (escribe 'x' para terminar):")
    nombre = input("Nombre: ")
    while nombre.lower() != "x" and (not nombre.isalpha() or len(nombre.strip()) == 0):
        nombres_secundaria.append(nombre)
        nombre = input("Nombre: ")
    # Proceso y salida
    nombres_primaria_unicos, nombres_secundaria_unicos = mostrar_alumnos(nombres_primaria, nombres_secundaria)
    nombres_repetidos = mostrar_nombres_repetidos(nombres_primaria_unicos, nombres_secundaria_unicos)
    nombres_no_rep_sec = mostrar_nomb_primaria_no_sec(nombres_primaria_unicos, nombres_secundaria_unicos)
    inclusion_primaria_secundaria = verificar_nomb_primaria_sec(nombres_primaria_unicos, nombres_secundaria_unicos)