class Vehiculo:
    def __init__(self, direccion):
        self.posicion = 0
        self.direccion = direccion  # "NS" o "EW"
        self.detenido = False

    def mover(self, semaforo):
        # Si el vehículo está detenido
        if self.detenido:
            # Revisa si el semáforo cambia a verde
            if semaforo.estado == "Verde":
                self.detenido = False
                self.posicion += 1
        # Si no está detenido, avanza
        else:
            # Se detiene si hay un semáforo en rojo en la posición 0
            if semaforo.estado == "Rojo" and self.posicion == 0:
                self.detenido = True
            else:
                self.posicion += 1