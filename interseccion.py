from vehiculo import Vehiculo
from semaforo import Semaforo

class Interseccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.semaforo_NS = Semaforo("NS")  # Semáforo para la dirección Norte-Sur
        self.semaforo_EW = Semaforo("EW")  # Semáforo para la dirección Este-Oeste
        self.vehiculos_NS = []
        self.vehiculos_EW = []
        
        # Parámetros de distancia para las reglas
        self.distancia_corta_r = 2  # Distancia corta R para la Regla 3
        self.distancia_mas_alla_e = 5 # Distancia más allá de la intersección E para Reglas 4 y 6

    def agregar_vehiculo(self, direccion):
        """Agrega un nuevo vehículo a la intersección en la dirección especificada."""
        if direccion == "NS":
            self.vehiculos_NS.append(Vehiculo("NS"))
        else:
            self.vehiculos_EW.append(Vehiculo("EW"))

    def actualizar_vehiculos(self):
        """Mueve todos los vehículos en la intersección según el estado de su semáforo."""
        for v in self.vehiculos_NS:
            v.mover(self.semaforo_NS)
        for v in self.vehiculos_EW:
            v.mover(self.semaforo_EW)

    def actualizar_semaforos(self):
        """Actualiza el estado de los semáforos basándose en las reglas de autoorganización."""
        
        # Vehículos esperando en rojo 
        esperando_NS = sum(1 for v in self.vehiculos_NS if v.detenido)
        esperando_EW = sum(1 for v in self.vehiculos_EW if v.detenido)

        # Vehículos a corta distancia de la intersección 
        cerca_NS = sum(1 for v in self.vehiculos_NS if 0 < v.posicion <= self.distancia_corta_r)
        cerca_EW = sum(1 for v in self.vehiculos_EW if 0 < v.posicion <= self.distancia_corta_r)

        # Vehículos detenidos más allá de la intersección
        detenidos_mas_alla_NS = any(v.detenido and v.posicion > self.distancia_mas_alla_e for v in self.vehiculos_NS)
        detenidos_mas_alla_EW = any(v.detenido and v.posicion > self.distancia_mas_alla_e for v in self.vehiculos_EW)

       
        if detenidos_mas_alla_NS and detenidos_mas_alla_EW:
            print(f"--- Intersección {self.nombre}: Alerta Regla 6 -> Vehículos detenidos en ambas direcciones. Ambos semáforos en ROJO. ---")
            self.semaforo_NS.estado = "Rojo"
            self.semaforo_EW.estado = "Rojo"
            return 
        else:
            if not detenidos_mas_alla_NS and self.semaforo_NS.estado == "Rojo":
                # print(f"--- Intersección {self.nombre}: Liberación de NS, restaurando a VERDE ---")
                self.semaforo_NS.estado = "Verde"
            if not detenidos_mas_alla_EW and self.semaforo_EW.estado == "Rojo":
                # print(f"--- Intersección {self.nombre}: Liberación de EW, restaurando a VERDE ---")
                self.semaforo_EW.estado = "Verde"

        
        self.semaforo_NS.actualizar(
            vehiculos_esperando=esperando_NS,
            vehiculos_cerca=cerca_NS,
            vehiculos_detenidos_mas_alla=detenidos_mas_alla_NS
        )
        self.semaforo_EW.actualizar(
            vehiculos_esperando=esperando_EW,
            vehiculos_cerca=cerca_EW,
            vehiculos_detenidos_mas_alla=detenidos_mas_alla_EW
        )

    def imprimir_estado(self):
        """Imprime el estado actual de la intersección y sus semáforos."""
        print(f"Intersección {self.nombre}:")
        print(f"  Semaforo NS: {self.semaforo_NS.estado}, Vehiculos esperando: {self.semaforo_NS.contador_vehiculos}")
        print(f"  Semaforo EW: {self.semaforo_EW.estado}, Vehiculos esperando: {self.semaforo_EW.contador_vehiculos}")
        print(f"  Total vehiculos NS: {len(self.vehiculos_NS)}, EW: {len(self.vehiculos_EW)}")