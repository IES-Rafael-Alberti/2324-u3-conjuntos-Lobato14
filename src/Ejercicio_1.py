# Suponer una lista con datos de las compras hechas por clientes de una empresa a lo 
# largo de un mes, la cual contiene tuplas con información de cada venta: (cliente, 
# día del mes, monto, domicilio del cliente). Ejemplo:

# [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 
# 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, 
# "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]

# Escribir una función que reciba como parámetro una lista con el formato mencionado 
# anteriormente y retorne los domicilios de cada cliente al cual se le debe enviar una 
# factura de compra. Notar que cada cliente puede haber hecho más de una compra en el 
# mes, por lo que la función debe retornar una estructura que contenga cada domicilio 
# una sola vez.

def obtener_domicilios_compra(lista_compras: list) -> list:
    """
    Obtiene los domicilios de los clientes a partir de una lista de compras.

    Parameters
    ----------
    - lista_compras : list
        Lista que contiene información de las compras, donde cada elemento es una tupla
        con la estructura (cliente, mes, monto, domicilio).

    Returns
    --------
    - list
        Lista de domicilios de los clientes.
    """
    domicilios = {}
    for compra in lista_compras:
        cliente, mes, monto, domicilio = compra
        domicilios[cliente] = domicilio
    return list(domicilios.values())


if __name__ == "__main__":
    # Entrada (lista de las compras)
    compras = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
            ("Jorge Russo", 7, 699, "Mirasol 218"),
            ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
            ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
            ("Jorge Russo", 15, 958, "Mirasol 218")]
    # Proceso
    domicilios_unicos = obtener_domicilios_compra(compras)
    # Salida
    print(domicilios_unicos)