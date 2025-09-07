class Vehiculo:
    def __init__(self, direccion):
        self.posicion = 0
        self.direccion = direccion  # "NS" o "EW"
        self.detenido = False

    def mover(self, semaforo):
        if self.detenido:
            # Revisar si semáforo verde
            if semaforo.estado == "Verde":
                self.detenido = False
                self.posicion += 1
        else:
            # Avanzar si semáforo verde o sin semáforo
            if semaforo.estado == "Rojo" and self.posicion == 0:
                self.detenido = True
            else:
                self.posicion += 1
    