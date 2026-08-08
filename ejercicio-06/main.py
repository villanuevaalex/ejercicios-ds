"""
Cree un programa que muestre un menú interactivo utilizando la estructura match.
    a. Calcular la suma de los primeros N números naturales (usando un for).
    b. Encontrar todos los números divisibles por 3 en un rango dado por el usuario. (Ver range())
    c. Salir.
"""
import os
    
def menu():
    os.system('clear')
    print("""
********************************************** MENU **************************************************
*                                                                                                    *
*   Elija una opción:                                                                                *
*   1) Calcular la suma de N números naturales (usando for)                                          *
*   2) Encontrar todos los números divisibles por 3 en un rango dado por el usuario. (ver range())   *
*   3) Salir                                                                                         *
*                                                                                                    *
******************************************************************************************************
    """)

def n_naturales(n:int):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print(f"La suma de los {n} números es: {suma}")

def divisibles_por_3(inicio:int, fin:int):
    divisibles = []
    for numero in range(inicio, fin + 1):
        if numero % 3 == 0:
            divisibles.append(numero)
    print(f"Los resultados son: {divisibles} ")

while True:
    menu()
    opcion = input("Introduzca opción: ")
    os.system('clear')

    match opcion:
        case "1":
            print("Sumar los primeros N números naturales\n")
            n = int(input("Ingrese N: "))
            n_naturales(n)
            input("\nPresione Enter para volver al menú...")
        case "2":
            print("Encontrar todos los números divisibles por 3 en un rango dado\n")
            inicio = int(input("Ingrese inicio de rango: "))
            fin = int(input("Ingrese fin de rango: "))
            divisibles_por_3(inicio, fin)
            input("\nPresione Enter para volver al menú...")
        case "3":
            break
        case _:
            print("Opción inválida, intente de nuevo\n")
            input("\nPresione Enter para volver al menú...")