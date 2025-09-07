# semaforo.py

class Semaforo:
    def __init__(self, direccion):
        self.direccion = direccion
        self.estado = "Rojo"  # Estado inicial: Rojo
        self.tiempo_verde = 0
        self.contador_vehiculos = 0  # Número de vehículos esperando en rojo
        self.umbral_cambio = 3       # Umbral N para cambiar el semáforo (Regla 1)
        self.tiempo_minimo = 2       # Tiempo mínimo en verde U (Regla 2)

    def actualizar(self, vehiculos_esperando, vehiculos_cerca, vehiculos_detenidos_mas_alla):
        """
        Aplica las reglas de autoorganización del semáforo.
        """
        self.contador_vehiculos = vehiculos_esperando
        
        if self.estado == "Verde":
            self.tiempo_verde += 1
            if self.tiempo_verde < self.tiempo_minimo:
                return # No cambiar si aún no se cumple el tiempo mínimo

        if self.estado == "Verde" and vehiculos_cerca <= 1 and not vehiculos_detenidos_mas_alla:
            return # No cambiar si solo hay un vehículo (o ninguno) intentando cruzar y no hay obstáculos

        if self.contador_vehiculos >= self.umbral_cambio:
            if self.estado == "Rojo": 
                self.estado = "Verde"
                self.tiempo_verde = 0 
                self.contador_vehiculos = 0
        else:
            if self.estado == "Verde":
                self.estado = "Rojo"
                self.tiempo_verde = 0