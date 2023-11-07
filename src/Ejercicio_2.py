# Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de 
# una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que 
# introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

# 1. Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
# 2. Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
# 3. Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
# 4. Mostrar si todos los nombres de primaria están incluidos en secundaria.

def obtener_nombres(nombres_primaria, nombres_secundaria):

    print("Introduce los nombres de los alumnos de primaria (escribe 'x' para terminar):")
    nombre = input("Nombre: ")
    while nombre.lower() != "x":
        nombres_primaria.append(nombre)
        nombre = input("Nombre: ")

    print("Introduce los nombres de los alumnos de secundaria (escribe 'x' para terminar):")
    nombre = input("Nombre: ")
    while nombre.lower() != "x":
        nombres_secundaria.append(nombre)
        nombre = input("Nombre: ")

    return nombres_primaria, nombres_secundaria

def mostrar_resultados(nombres_primaria, nombres_secundaria):
    # Mostrar nombres de todos los alumnos de primaria y secundaria sin repeticiones
    print("\nNombres de todos los alumnos de primaria:")
    nombres_primaria_unicos = list(set(nombres_primaria))
    print(nombres_primaria_unicos)
    
    print("\nNombres de todos los alumnos de secundaria:")
    nombres_secundaria_unicos = list(set(nombres_secundaria))
    print(nombres_secundaria_unicos)

    # Mostrar nombres que se repiten entre primaria y secundaria
    print("\nNombres que se repiten entre primaria y secundaria:")
    nombres_repetidos = list(set(nombres_primaria_unicos) & set(nombres_secundaria_unicos))
    print(nombres_repetidos)

    # Mostrar nombres de primaria que no se repiten en secundaria
    print("\nNombres de primaria que no se repiten en secundaria:")
    nombres_no_repetidos = list(set(nombres_primaria_unicos) - set(nombres_secundaria_unicos))
    print(nombres_no_repetidos)

    # Verificar si todos los nombres de primaria están incluidos en secundaria
    if set(nombres_primaria_unicos).issubset(set(nombres_secundaria_unicos)):
        print("\nTodos los nombres de primaria están incluidos en secundaria.")
    else:
        print("\nNo todos los nombres de primaria están incluidos en secundaria.")

if __name__ == "__main__":
    nombres_primaria = []
    nombres_secundaria = []
    nombres_primaria, nombres_secundaria = obtener_nombres(nombres_primaria, nombres_secundaria)
    mostrar_resultados(nombres_primaria, nombres_secundaria)