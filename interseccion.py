from vehiculo import Vehiculo
from semaforo import Semaforo

class Interseccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.semaforo_NS = Semaforo("NS")
        self.semaforo_EW = Semaforo("EW")
        self.vehiculos_NS = []
        self.vehiculos_EW = []

    def agregar_vehiculo(self, direccion):
        if direccion == "NS":
            self.vehiculos_NS.append(Vehiculo("NS"))
        else:
            self.vehiculos_EW.append(Vehiculo("EW"))

    def actualizar_vehiculos(self):
        for v in self.vehiculos_NS:
            v.mover(self.semaforo_NS)
        for v in self.vehiculos_EW:
            v.mover(self.semaforo_EW)

    def actualizar_semaforos(self):
        self.semaforo_NS.actualizar(
            vehiculos_esperando=sum(1 for v in self.vehiculos_NS if v.detenido)
        )
        self.semaforo_EW.actualizar(
            vehiculos_esperando=sum(1 for v in self.vehiculos_EW if v.detenido)
        )

    def imprimir_estado(self):
        print(f"Interseccion {self.nombre}:")
        print(f"  Semaforo NS: {self.semaforo_NS.estado}, Vehiculos esperando: {sum(1 for v in self.vehiculos_NS if v.detenido)}")
        print(f"  Semaforo EW: {self.semaforo_EW.estado}, Vehiculos esperando: {sum(1 for v in self.vehiculos_EW if v.detenido)}")
        print(f"  Total vehiculos NS: {len(self.vehiculos_NS)}, EW: {len(self.vehiculos_EW)}\n")
