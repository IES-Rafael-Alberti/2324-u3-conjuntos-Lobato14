from src.Ejercicio_1 import obtener_domicilios_compra

def test_obtener_domicilios_compra():
    compras = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
               ("Jorge Russo", 7, 699, "Mirasol 218"),
               ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
               ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
               ("Jorge Russo", 15, 958, "Mirasol 218")]
    
    domicilios_unicos = obtener_domicilios_compra(compras)
    
    assert len(domicilios_unicos) == 3
    assert "Calle Las Flores 355" in domicilios_unicos
    assert "Mirasol 218" in domicilios_unicos
    assert "La Mancha 761" in domicilios_unicos