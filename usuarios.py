class Usuario:
    def __init__(self, nombre,saldo_inicial = 0):
        self.nombre = nombre
        self.saldo = saldo_inicial
    def hacer_deposito(self, amount):
            self.saldo += amount
            print(f"Se hizo un deposito de {amount} .")
    def hacer_retiro(self, cantidad) :
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Se retiro la suma de  {cantidad} .")
            else:
                print("Fondos insuficientes. No se pudo realizar el retiro.")
    def mostrar_balance_usuario(self):
                print(f"Saldo actual de {self.nombre}: {self.saldo}")

usuario_1= Usuario("usuario_1")
usuario_2=Usuario("usuario_2")
usuario_3=Usuario("usuario_3")

usuario_1.hacer_deposito(100)
usuario_1.hacer_deposito(200)
usuario_1.hacer_deposito(500)
usuario_1.hacer_retiro(100)
usuario_1.mostrar_balance_usuario()

usuario_2.hacer_deposito(500)
usuario_2.hacer_deposito(600)
usuario_2.hacer_retiro(100)
usuario_2.hacer_retiro(150)
usuario_2.mostrar_balance_usuario()

usuario_3.hacer_deposito(400)
usuario_3.hacer_retiro(50)
usuario_3.hacer_retiro(20)
usuario_3.hacer_retiro(200)
usuario_3.mostrar_balance_usuario()

