"""
El programa debe calcular el costo total del viaje y determinar 
(con un booleano) si el dinero disponible es suficiente. 
Muestra un resumen formateado con los resultados. 
Ver input() y f-strings.
"""

# Escriba un programa que solicite al usuario: 
# a. El costo estimado de un pasaje,
# b. El costo de alojamiento por noche,
# c. La cantidad de noches que durará el viaje 
# d. El dinero disponible.

def calculo_costos(c_alojamiento, c_noches, c_pasajes, dinero_disponble):
    costo_total = c_noches * c_alojamiento + c_pasajes
    print(f"COSTO TOTAL: {costo_total}")
    return dinero_disponble > costo_total

costo_pasaje = float(input("ingrese costo estimado de pasaje: "))
costo_alojamiento = float(input("ingrese costo alojamiento p/noche: "))
cant_noches = int(input("ingrese cantidad de noches: "))
dinero_disp = float(input("ingrese dinero disponible ($): "))

print("\n------- CALCULO DE COSTOS -------")
print(f"Costo estimado de pasaje: {costo_pasaje}")
print(f"Costo alojamiento p/noche: {costo_alojamiento}")
print(f"Cantidad de noches: {cant_noches}")
print(f"Dinero disponible ($): {cant_noches}")
print("\nRESULTADO: ")
if (calculo_costos(costo_alojamiento, cant_noches, costo_pasaje, dinero_disp)):
    print("Es suficiente")
else:
    print("No es suficiente")
