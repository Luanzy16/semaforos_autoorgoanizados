class Vehiculo:
    def __init__(self, direccion):
        self.direccion = direccion  # "NS" o "EW" - dirección de movimiento del vehiculo
        self.pos = 0  # distancia relativa en la cola (simplificado)

    def mover(self):
        #Simula el movimiento del vehiculo incrementando su posición
        self.pos += 1 #Incremente de a 1 
