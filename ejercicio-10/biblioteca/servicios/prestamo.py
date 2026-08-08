from biblioteca.modelos.libro import Libro

def realizar_prestamo(libro:Libro):
    if libro.disponible:
        libro.disponible = False
        return f"Prestamo realizado correctamente: {libro.titulo}"
    else:
        return f"El libro '{libro.titulo}' no se encuentra disponible"

def realizar_devolucion(libro:Libro):
    if not libro.disponible:
        libro.disponible = True
        return f"Devolución realizada correctamente: {libro.titulo}"
    else:
        return f"El libro '{libro.titulo}' se encuentra disponible"
    

def consultar_disponibilidad(libro:Libro):
    if libro.disponible:
        return f"El libro '{libro.titulo}' se encuentra disponible"
    else:
        return f"El libro '{libro.titulo}' no se encuentra disponible"

