# Dado el conjunto de letras:

# vocales = {'a', 'e', 'i', 'o', 'u'}

# 1. Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
# 2. Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto 
# vocales como en el conjunto consonantes.

def encontrar_consonantes():
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = alfabeto - vocales
    return consonantes

def encontrar_letras_comunes(consonantes, vocales):
    letras_comunes = vocales.intersection(consonantes)
    return letras_comunes

if __name__ == "__main__":
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = encontrar_consonantes()
    letras_comunes = encontrar_letras_comunes(consonantes, vocales)

    print("Conjunto de consonantes:", consonantes)
    print("Conjunto de letras comunes:", letras_comunes)