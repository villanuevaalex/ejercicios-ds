"""
Escriba un programa que permita hacer la conversión de valores de temperatura 
entre Celsius y Fahrenheit. 
Se debe solicitar al usuario que ingrese un valor numérico y la escala original.
El programa deberá mostrar por pantalla el valor convertido 
incluyendo la escala final. 
Ver input(). 
Construya dos funciones, 
una para convertir datos a escala Celsius 
y otra para convertir los datos a escala Fahrenheit.
"""

#  F -> C Fórmula 
# (32 °F − 32) × 5/9 = 0 °C
def convertir_a_Celsius(valor):
    return float((valor - 32) * (5/9))

#  C -> F 
# Fórmula (0 °C × 9/5) + 32 = 32 °F
def convertir_a_Fahrenheit(valor):
    return float((valor * (9/5) + 32))


value = float(input("ingrese valor a convertir (solo numero): "))
escala = input("Igrese tipo de estala Celsius (C) o Fahrenheit (F): ").upper()

if escala == 'F':
    print("\nCalculo de Fahrenheit a Celsius: ")
    conversion = convertir_a_Celsius(value)
    print(f"Resultado de la conversion ({value:.2f}°F) a Celsius: {conversion:.2f}°C")
else:
    print("\nCalculo de Celsius a Fahrenheit: ")
    conversion = convertir_a_Fahrenheit(value)
    print(f"Resultado de la conversion ({value:.2f}°F) a Celsius: {conversion:.2f}°C")
