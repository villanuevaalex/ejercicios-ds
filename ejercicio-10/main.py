from biblioteca.modelos.libro import Libro
from biblioteca.servicios.prestamo import realizar_devolucion, realizar_prestamo, consultar_disponibilidad

libro1 = Libro("Hannibal")

print(consultar_disponibilidad(libro1))
print(realizar_prestamo(libro1))
print(realizar_prestamo(libro1))  
print(realizar_devolucion(libro1))
print(realizar_devolucion(libro1))
print(consultar_disponibilidad(libro1))