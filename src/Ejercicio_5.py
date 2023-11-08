# Dado el conjunto de números enteros:

# numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 1. Crea un conjunto pares que contenga los números pares del conjunto numeros.
# 2. Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos 
# de tres del conjunto numeros.
# 3. Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y 
# guárdala en un conjunto llamado pares_y_multiplos_de_tres.

# Función para crear un conjunto de números pares
def conjunto_pares(numeros):
    pares = {num for num in numeros 
             if num % 2 == 0}
    return pares

# Función para crear un conjunto de números múltiplos de tres
def multiplos_tres(numeros):
    multiplos_de_tres = {num for num in numeros 
                         if num % 3 == 0}
    return multiplos_de_tres

# Función para encontrar la intersección entre los conjuntos pares y multiplos_de_tres
def intersecion_pares_multiplos(numeros):
    numeros_pares = conjunto_pares(numeros)
    numeros_mult_tres = multiplos_tres(numeros)
    pares_y_multiplos_de_tres = numeros_pares.intersection(numeros_mult_tres)
    return pares_y_multiplos_de_tres

if __name__ == "__main__":
    # Entrada
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # Proceso
    pares_y_multiplos_de_tres = intersecion_pares_multiplos(numeros)
    # Salida
    print("Números pares:", conjunto_pares(numeros))
    print("Números múltiplos de tres:", multiplos_tres(numeros))
    print("Intersección entre pares y múltiplos de tres:", pares_y_multiplos_de_tres)