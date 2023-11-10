# Dado el conjunto de letras:

# vocales = {'a', 'e', 'i', 'o', 'u'}

# 1. Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
# 2. Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto 
# vocales como en el conjunto consonantes.

def encontrar_consonantes() -> set:
    """
    Encuentra las consonantes en el alfabeto.

    Returns:
    - set
        Conjunto de consonantes en el alfabeto.
    """
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = alfabeto - vocales
    return consonantes

def encontrar_letras_comunes(consonantes: set, vocales: set) -> set:
    """
    Encuentra las letras comunes entre consonantes y vocales.

    Parameters:
    - consonantes : set
        Conjunto de consonantes.
    - vocales : set
        Conjunto de vocales.

    Returns:
    - set
        Conjunto de letras comunes entre consonantes y vocales.
    """
    letras_comunes = vocales.intersection(consonantes)
    return letras_comunes

if __name__ == "__main__":
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = encontrar_consonantes()
    letras_comunes = encontrar_letras_comunes(consonantes, vocales)

    print("Conjunto de consonantes:", consonantes)
    print("Conjunto de letras comunes:", letras_comunes)