class Semaforo:
    def __init__(self, direccion):
        self.direccion = direccion
        self.estado = "Rojo"
        self.tiempo_verde = 0
        self.contador_vehiculos = 0
        # Parámetros por defecto para las reglas
        self.umbral_cambio = 3
        self.tiempo_minimo = 2

    def actualizar(self, vehiculos_esperando, vehiculos_cerca):
        """
        Aplicar reglas de autoorganización
        """
        self.contador_vehiculos = vehiculos_esperando
        
        # Regla 2: Mantener un tiempo mínimo en verde
        if self.estado == "Verde":
            self.tiempo_verde += 1
            if self.tiempo_verde < self.tiempo_minimo:
                return

        # Regla 3: Si pocos vehículos van a cruzar, no cambiar a rojo
        if self.estado == "Verde" and vehiculos_cerca <= 1:
            return

        # Regla 1: Cambiar si hay suficientes vehículos esperando en la otra dirección
        if self.contador_vehiculos >= self.umbral_cambio:
            if self.estado == "Rojo":
                self.estado = "Verde"
                self.tiempo_verde = 0
                self.contador_vehiculos = 0 # Reiniciar contador al cambiar
        else:
            if self.estado == "Verde":
                self.estado = "Rojo"
                self.tiempo_verde = 0