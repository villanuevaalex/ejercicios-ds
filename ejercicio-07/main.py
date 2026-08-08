"""
Escribe un programa con una función llamada analizar_temperaturas(registros) 
que reciba una lista de números (temperaturas).
    a. La función debe retornar en una sola tupla: 
    el valor máximo, el valor mínimo y el promedio de las temperaturas. 
    (ver operaciones con listas)
    b. Invocar a la función con datos de prueba 
    e imprimir los resultados desmpaquetándolos.
"""

def analizar_temperaturas(registros):
    maximo = max(registros)
    minimo = min(registros)
    promedio = sum(registros)/len(registros)
    list_analizada = [maximo, minimo, promedio]
    return list_analizada

LISTA = [1.2, 4.5, 3.4, 3.0, 9.89, 10.68, 6.98, 7.45]

print(f"\nLista a analizar: {LISTA}")

new_list = analizar_temperaturas(LISTA)
maximo, minimo, prom = new_list
print(f"""
Elemento maximo de la lista:                    {maximo:.2f}
Elemento minimo de la lista:                    {minimo:.2f} 
Valor promedio de los elementos de la lista:    {prom:.2f}
""")