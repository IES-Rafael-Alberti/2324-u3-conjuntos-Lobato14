# El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.
# Por ejemplo, el conjunto potencia de {1,2,3} es:

# {∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}

# Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera 
# s y retorne su «lista potencia» (la lista de todos sus subconjuntos):

# >>> conjunto_potencia({6, 1, 4})
# [set(), set([6]), set([1]), set([4]), set([6, 1]), 
# set([6, 4]), set([1, 4]), set([6, 1, 4])]

def conjunto_potencia(s):
    elementos = list(s)
    total_elementos = len(elementos)
    total_subconjuntos = 1 << total_elementos
    potencia = [set() for _ in range(total_subconjuntos)]

    for subconjunto_numero in range(total_subconjuntos):
        for elemento_numero in range(total_elementos):
            if (subconjunto_numero >> elemento_numero) & 1:
                potencia[subconjunto_numero].add(elementos[elemento_numero])
    return potencia

if __name__ == "__main__":
    # Entrada
    conjunto_original = {1, 2, 3}
    # Proceso
    lista_potencia = conjunto_potencia(conjunto_original)
    # Salida
    print(lista_potencia)