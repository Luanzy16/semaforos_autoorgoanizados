class Semaforo:
    def __init__(self, direccion):
        self.direccion = direccion
        self.estado = "Rojo"
        self.tiempo_verde = 0
        self.contador = 0

    def actualizar(self, vehiculos_esperando, umbral_cambio=3, tiempo_minimo=2):
        """
        Aplicar reglas de autoorganizacion
        """
        self.contador = vehiculos_esperando

        # Regla 1: tiempo minimo en verde
        if self.estado == "Verde":
            self.tiempo_verde += 1
            if self.tiempo_verde < tiempo_minimo:
                return

        # Regla 2: cambiar si hay suficientes vehiculos esperando
        if self.contador >= umbral_cambio:
            self.estado = "Verde"
            self.tiempo_verde = 0
        else:
            self.estado = "Rojo"

