"""
Crea una clase CuentaBancaria con los siguientes requisitos:
    a. Atributos de instancia: titular y saldo (por defecto en 0.0).
    b. Método depositar(monto): suma el monto al saldo si es mayor a 0.
    c. Método retirar(monto): resta el saldo si hay fondos suficientes, 
        de lo contrario muestra un mensaje de error.
    d. Método mostrar_info(): imprime el titular y el saldo actual.
Crea un par de instancias y realizar operaciones para probarla.
"""

class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto

    def retirar(self,monto):
        if self.saldo >= monto:
            self.saldo -= monto
        else:
            print("Fondos insuficientes")

    def mostrar_info(self):
        print(f"\nTitular:     {self.titular}")
        print(f"Saldo:      {self.saldo}")


# PRUEBAS

cuenta1 = CuentaBancaria("Alex")
cuenta2 = CuentaBancaria("Meli", 500)

cuenta1.depositar(100)
cuenta1.mostrar_info()

cuenta2.retirar(1000)  
cuenta2.mostrar_info()

cuenta1.retirar(50)    
cuenta1.mostrar_info()

cuenta1.depositar(-20) 
cuenta1.mostrar_info()