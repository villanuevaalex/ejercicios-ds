"""
Escriba un programa que simule un inicio de sesión. 
Definir una contraseña correcta en una constante (ej. "Admin1234").
    a. Permitir al usuario intentar ingresarla un máximo de 3 veces usando un bucle while.
    b. Si acierta, muestra un mensaje de éxito y termina.
    c. Si agota los intentos, muestra un mensaje de
    bloqueo y finaliza el programa.
"""

PASSWORD = "Admin1234"
i = 1

while True:
    password = input("\nIngrese contraseña: ")
    i += 1
    if password == PASSWORD:
        print("Contraseña correcta!")
        break
    else:
        print("Contraseña equivocada, vuelve a intentarlo")

    if i > 3:
        print("\nHas excedido el máximo de intentos permitidos (3 intentos)") 
        break