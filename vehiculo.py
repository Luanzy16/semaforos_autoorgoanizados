class Vehiculo:
    def __init__(self, direccion):
        self.direccion = direccion  # "NS" o "EW"
        self.pos = 0  # distancia relativa en la cola (simplificado)

    def mover(self):
        """En animación podría mover su posición; aquí placeholder."""
        self.pos += 1
