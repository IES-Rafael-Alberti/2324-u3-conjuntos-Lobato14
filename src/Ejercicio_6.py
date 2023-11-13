# Dado el conjunto de letras:

# vocales = {'a', 'e', 'i', 'o', 'u'}

# 1. Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
# 2. Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto 
# vocales como en el conjunto consonantes.

def encontrar_consonantes() -> set:
    """
    Encuentra las consonantes en el alfabeto.

    Returns
    -------
    - set:
        Conjunto de consonantes en el alfabeto.
    """
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = alfabeto - vocales
    return consonantes

def obtener_palabra_valida() -> str:
    """
    Solicita al usuario que introduzca una palabra válida (solo letras).

    Returns
    -------
    - str:
        Palabra válida introducida por el usuario.
    """
    palabra = input("Introduce una palabra: ").lower()
    while not palabra.isalpha():
        palabra = input("Por favor, introduce solo letras. Vuelve a intentarlo: ").lower()
    return palabra

def encontrar_letras_comunes(palabra: str, consonantes: set, vocales: set) -> set:
    """
    Encuentra las letras comunes entre consonantes y vocales en una palabra.

    Parameters
    ----------
    - palabra : str
        Palabra de entrada.
    - consonantes : set
        Conjunto de consonantes.
    - vocales : set
        Conjunto de vocales.

    Returns
    --------
    - set:
        Conjunto de letras comunes entre consonantes y vocales en la palabra.
    """
    letras_palabra = set(letra for letra in palabra if letra.isalpha())
    letras_consonantes = letras_palabra.intersection(consonantes)
    return letras_palabra, letras_consonantes

if __name__ == "__main__":
    # Entrada
    vocales = {'a', 'e', 'i', 'o', 'u'}
    # Procesamiento
    consonantes = encontrar_consonantes()
    palabra = obtener_palabra_valida()
    letras_palabra, letras_consonantes = encontrar_letras_comunes(palabra, consonantes, vocales)
    # Salida
    print("Conjunto de consonantes:", consonantes)
    print("Conjunto de letras en la palabra:", letras_palabra)
    print("Conjunto de consonantes en la palabra:", letras_consonantes)