# cliente.py
class Cliente:
    def __init__(self, nombre, empresa, cantidad_ventanas):
        self.nombre = nombre
        self.empresa = empresa
        self.cantidad_ventanas = cantidad_ventanas
        self.tipo_cliente = self.validar_tipo_cliente()

    def validar_tipo_cliente(self):
        if "empresa" in self.empresa.lower():
            return "Empresa"
        return "Cliente Individual"
