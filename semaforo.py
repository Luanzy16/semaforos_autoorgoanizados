class Semaforo:
    def __init__(self, direccion, tiempo_minimo=3, max_rojo=8):
        self.direccion = direccion  # "NS" o "EW"
        self.estado = "rojo"
        self.tiempo_verde_actual = 0
        self.tiempo_rojo = 0

        # Parámetros de reglas
        self.tiempo_minimo = tiempo_minimo
        self.max_rojo = max_rojo

    def poner_verde(self):
        self.estado = "verde"
        self.tiempo_verde_actual = 0
        self.tiempo_rojo = 0

    def poner_rojo(self):
        self.estado = "rojo"
        self.tiempo_verde_actual = 0
        self.tiempo_rojo = 0

    def actualizar(self, en_verde):
        """Actualiza contadores según el estado."""
        if self.estado == "verde":
            self.tiempo_verde_actual += 1
        else:
            self.tiempo_rojo += 1
