import sys

# argv[0] es el nombre del script, argv[1] es el primer argument
# NOTA: no sirve sys.argv[1] != None, porque python evalúa antes de comparar
if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    arg = "Pepe"

print("hola", arg, sep=" ", end="!!!\n")