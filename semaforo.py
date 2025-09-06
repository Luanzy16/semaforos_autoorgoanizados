class Semaforo:
    def __init__(self, direccion, verde=True, u=5):
        self.direccion = direccion
        self.verde = verde
        self.tiempo_verde = 0
        self.u = u  # tiempo mínimo en verde
        self.contador = 0  # vehículos esperando en rojo

    def cambiar(self, nuevo_estado=None):
        """Cambia el semáforo (verde/rojo)."""
        if nuevo_estado is None:
            self.verde = not self.verde
        else:
            self.verde = nuevo_estado
        self.contador = 0
        self.tiempo_verde = 0

    def paso(self):
        """Aumenta el contador de tiempo en verde."""
        if self.verde:
            self.tiempo_verde += 1
