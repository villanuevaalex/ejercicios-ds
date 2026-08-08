"""
Escriba un programa que solicite al usuario una contraseña. 
Utilizar operadores lógicos y métodos de strings (.isupper(), .islower(), len()) 
para verificar si cumple con tres condiciones básicas:
    a. Tiene al menos 8 caracteres,
    b. Contiene al menos una letra mayúscula
    c. Al menos una minúscula. 
Imprimir un mensaje adecuado al caso.
"""

def tiene_mayuscula(password):
    resultados = [c.isupper() for c in password]
    # si dentro de resultados hay al menos un True devuelve True
    return any(resultados) 

def tiene_minuscula(password):
    resultados = [c.islower() for c in password]
    # si dentro de resultados hay al menos un True devuelve True
    return any(resultados)

def validar_password(password):
    condiciones = [
        len(password) >= 8,
        tiene_mayuscula(password),
        tiene_minuscula(password),
    ]
    # si dentro de resultados todos son True devuelve True
    return all(condiciones)

while True:
    password = input("Escriba su contraseña: ")
    if validar_password(password):
        break
    if len(password) < 8:
        print("Contraseña con menos de 8 caracteres")
    elif not tiene_mayuscula(password):
        print("Contraseña sin mayusculas")
    elif not tiene_minuscula(password):
        print("Contraseña sin minusculas")    

print("\nContraseña CORRECTA!")