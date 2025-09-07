from interseccion import Interseccion
import random

class Simulacion:
    def __init__(self):
        # 4 intersecciones: A, B, C, D
        self.intersecciones = [
            Interseccion("A"), Interseccion("B"),
            Interseccion("C"), Interseccion("D")
        ]
        self.tiempo = 0

    def agregar_vehiculos(self):
        for inter in self.intersecciones:
            # Cada paso, llega 0 a 2 vehiculos por direccion
            for _ in range(random.randint(0, 2)):
                inter.agregar_vehiculo("NS")
            for _ in range(random.randint(0, 2)):
                inter.agregar_vehiculo("EW")

    def paso(self):
        print(f"--- Paso {self.tiempo} ---")
        self.agregar_vehiculos()
        for inter in self.intersecciones:
            inter.actualizar_vehiculos()
            inter.actualizar_semaforos()
            inter.imprimir_estado()
        self.tiempo += 1
