"""
8. Escribir un programa que contenga una función 
    calcular_precio_final(precio_base, porcentaje_descuento=10, es_vip=False).
    a. Si el cliente es VIP (es_vip=True), se le descuenta un
        5% extra sobre el precio ya rebajado.
    b. Validar que los valores ingresados sean positivos
        (lanzar una excepción ValueError si esto no es así).
Invocar a la función varias veces con diferentes parámetros 
para comprobar el funcionamiento correcto.
"""

import unittest

def calcular_precio_final(precio_base, porcentaje_descuento=10, es_vip=False):
    if precio_base < 0 or porcentaje_descuento < 0:
        raise ValueError("El precio base y procentaje de descuento deben ser positivos")

    precio_base = precio_base * (1-porcentaje_descuento/100)
    if es_vip:
        return precio_base * 0.95
    
    return precio_base


print("--- Pruebas ---\n")

class TestCalcularPrecioFinal(unittest.TestCase):

    def test_descuento_por_defecto(self):
        # por defecto descuento 10% y vip=false
        # unicamente descuento del 10% = 100 - 10
        self.assertEqual(calcular_precio_final(100), 90)

    def test_con_descuento_personalizado(self):
        # descuento 20% y vip=false
        # unicamente descuento del 20% = 100 - 20
        self.assertEqual(calcular_precio_final(100, 20), 80)

    def test_vip_aplica_extra(self):
        # descuento 20% y vip=true
        # unicamente descuento del 20% = 100 - 20 = 80
        # 80 * 0.95 
        resultado = calcular_precio_final(100, 20, True)
        self.assertAlmostEqual(resultado, 76.0)  

    def test_precio_negativo_lanza_excepcion(self):
        # precio base en negativo, tiene que detectarse ValueError 
        with self.assertRaises(ValueError):
            calcular_precio_final(-50)

if __name__ == "__main__":
    unittest.main()