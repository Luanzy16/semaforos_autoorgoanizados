class Vehiculo:
    def __init__(self, posicion, direccion):
        self.posicion = posicion  # distancia a la intersección (0 = en la línea)
        self.direccion = direccion  # "N" o "E"
        self.detenido = False

    def mover(self):
        """Avanza hacia la intersección si no está detenido."""
        if not self.detenido:
            self.posicion -= 1
