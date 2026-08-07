import logging

# para setear el nivel de visualizacion de logging
# Los niveles van de menor a mayor severidad: 
# DEBUG < INFO < WARNING < ERROR < CRITICAL
logging.basicConfig(level=logging.DEBUG) 

# la manera más simple 
print("hola mundo")

"""
otra forma de 
escribir un
print
"""

print("Hola", "Mundo", sep=", ", end="!\n")

# este logging es para mosrar distintos tipos de logging de la aplicación 

logging.debug("Mensaje de depuración")
logging.info("Información general")
logging.warning("Algo raro pasó, pero no es grave")
logging.error("Ocurrió un error")
logging.critical("Error crítico, el programa puede fallar")

"""
SALIDA POR TERMINAL: 
hola mundo
Hola, Mundo!
WARNING:root:Algo raro pasó, pero no es grave
ERROR:root:Ocurrió un error
CRITICAL:root:Error crítico, el programa puede fallar
"""