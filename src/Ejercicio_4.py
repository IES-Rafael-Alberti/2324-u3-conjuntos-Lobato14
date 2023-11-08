# Dadas las siguientes listas:

# frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
# frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

# 1. Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
# 2. Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto 
# llamado frutas_comunes.
# 3. Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un 
# conjunto llamado frutas_solo_en_frutas1.
# 4. Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un 
# conjunto llamado frutas_solo_en_frutas2.

# Función para encontrar las frutas que están en ambas listas
def encontrar_frutas_ambos(set_frutas1, set_frutas2):
    frutas_comunes = set_frutas1.intersection(set_frutas2)
    return frutas_comunes

# Función para encontrar las frutas que están en frutas1 pero no en frutas2
def solo_frutas_1(set_frutas1, set_frutas2):
    frutas_comunes = set_frutas1.intersection(set_frutas2)
    frutas_solo_en_frutas1 = set_frutas1 - frutas_comunes
    return frutas_solo_en_frutas1

# Función para encontrar las frutas que están en frutas2 pero no en frutas1
def solo_frutas_2(set_frutas1, set_frutas2):
    frutas_solo_en_frutas2 = set_frutas2.difference(set_frutas1)
    return frutas_solo_en_frutas2

if __name__ == "__main__":
    # Entrada
    set_frutas1 = set(["manzana", "pera", "naranja", "plátano", "uva"])
    set_frutas2 = set(["manzana", "pera", "durazno", "sandía", "uva"])
    # Proceso
    resultado_ambas_frutas = encontrar_frutas_ambos(set_frutas1, set_frutas2)
    resultado_solo_frutas_1 = solo_frutas_1(set_frutas1, set_frutas2)
    resultado_solo_futas_2 = solo_frutas_2(set_frutas1, set_frutas2)
    # Salida
    print("Frutas comunes en ambas listas:", resultado_ambas_frutas)
    print("Frutas solo en frutas1:", resultado_solo_frutas_1)
    print("Frutas solo en frutas2:", resultado_solo_futas_2)