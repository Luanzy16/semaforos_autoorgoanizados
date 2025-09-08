from vehiculo import Vehiculo
from semaforo import Semaforo

class Interseccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.semaforo_NS = Semaforo("NS")
        self.semaforo_EW = Semaforo("EW")
        self.vehiculos_NS = []
        self.vehiculos_EW = []
        # Parámetros para las reglas
        self.distancia_corta_r = 2
        self.distancia_mas_alla_e = 5

    def agregar_vehiculo(self, direccion):
        if direccion == "NS":
            self.vehiculos_NS.append(Vehiculo("NS"))
        else:
            self.vehiculos_EW.append(Vehiculo("EW"))

    def actualizar_vehiculos(self):
        # Mover vehículos
        for v in self.vehiculos_NS:
            v.mover(self.semaforo_NS)
        for v in self.vehiculos_EW:
            v.mover(self.semaforo_EW)

        # Eliminar vehículos que ya cruzaron la intersección (para simular el flujo)
        self.vehiculos_NS = [v for v in self.vehiculos_NS if v.posicion <= 20] # Se mantiene por 20 pasos de tiempo
        self.vehiculos_EW = [v for v in self.vehiculos_EW if v.posicion <= 20]

    def actualizar_semaforos(self):
        # Recopilar datos de tráfico
        esperando_NS = sum(1 for v in self.vehiculos_NS if v.detenido)
        esperando_EW = sum(1 for v in self.vehiculos_EW if v.detenido)

        cerca_NS = sum(1 for v in self.vehiculos_NS if 0 < v.posicion <= self.distancia_corta_r)
        cerca_EW = sum(1 for v in self.vehiculos_EW if 0 < v.posicion <= self.distancia_corta_r)

        detenidos_mas_alla_NS = any(v.detenido and v.posicion > self.distancia_mas_alla_e for v in self.vehiculos_NS)
        detenidos_mas_alla_EW = any(v.detenido and v.posicion > self.distancia_mas_alla_e for v in self.vehiculos_EW)

        # Regla 6: Lógica para vehículos detenidos en ambas direcciones
        if detenidos_mas_alla_NS and detenidos_mas_alla_EW:
            self.semaforo_NS.estado = "Rojo"
            self.semaforo_EW.estado = "Rojo"
            return
        
        # Regla 4: Lógica para vehículos detenidos en una sola dirección
        if detenidos_mas_alla_NS:
            self.semaforo_NS.estado = "Rojo"
        if detenidos_mas_alla_EW:
            self.semaforo_EW.estado = "Rojo"
            
        # Lógica de actualización normal
        self.semaforo_NS.actualizar(
            vehiculos_esperando=esperando_NS,
            vehiculos_cerca=cerca_NS
        )
        self.semaforo_EW.actualizar(
            vehiculos_esperando=esperando_EW,
            vehiculos_cerca=cerca_EW
        )

    def imprimir_estado(self):
        print(f"Interseccion {self.nombre}:")
        print(f"  Semaforo NS: {self.semaforo_NS.estado}, Vehiculos esperando: {self.semaforo_NS.contador_vehiculos}")
        print(f"  Semaforo EW: {self.semaforo_EW.estado}, Vehiculos esperando: {self.semaforo_EW.contador_vehiculos}")
        print(f"  Total vehiculos NS: {len(self.vehiculos_NS)}, EW: {len(self.vehiculos_EW)}\n")