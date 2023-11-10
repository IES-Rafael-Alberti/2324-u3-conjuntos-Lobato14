# Dado el conjunto de números enteros:

# numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 1. Crea un conjunto pares que contenga los números pares del conjunto numeros.
# 2. Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos 
# de tres del conjunto numeros.
# 3. Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y 
# guárdala en un conjunto llamado pares_y_multiplos_de_tres.

def conjunto_pares(numeros: set) -> set:
    """
    Crea un conjunto de números pares.

    Parameters:
    - numeros : set
        Conjunto de números.

    Returns:
    - set
        Conjunto de números pares.
    """
    pares = {num for num in numeros if num % 2 == 0}
    return pares

def multiplos_tres(numeros: set) -> set:
    """
    Crea un conjunto de números múltiplos de tres.

    Parameters:
    - numeros : set
        Conjunto de números.

    Returns:
    - set
        Conjunto de números múltiplos de tres.
    """
    multiplos_de_tres = {num for num in numeros if num % 3 == 0}
    return multiplos_de_tres

def interseccion_pares_multiplos(numeros: set) -> set:
    """
    Encuentra la intersección entre los conjuntos de números pares y múltiplos de tres.

    Parameters:
    - numeros : set
        Conjunto de números.

    Returns:
    - set
        Conjunto de números que son pares y múltiplos de tres.
    """
    numeros_pares = conjunto_pares(numeros)
    numeros_mult_tres = multiplos_tres(numeros)
    pares_y_multiplos_de_tres = numeros_pares.intersection(numeros_mult_tres)
    return pares_y_multiplos_de_tres


if __name__ == "__main__":
    # Entrada
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # Proceso
    pares = conjunto_pares(numeros)
    multiplos = multiplos_tres(numeros)
    interseccion = interseccion_pares_multiplos(numeros)
    # Salida
    print("Números pares:", pares)
    print("Números múltiplos de tres:", multiplos)
    print("Intersección entre pares y múltiplos de tres:", interseccion)
