from interseccion import Interseccion
import random

class Simulacion:
    def __init__(self):
        # Inicializa 4 intersecciones con nombres A, B, C, D.
        self.intersecciones = [
            Interseccion("A"), Interseccion("B"),
            Interseccion("C"), Interseccion("D")
        ]
        self.tiempo = 0  

    def agregar_vehiculos(self):
        """Agrega vehículos aleatoriamente a cada intersección en cada paso."""
        for inter in self.intersecciones:
            # Cada paso, se agregan entre 0 y 2 vehículos por cada dirección (NS y EW).
            for _ in range(random.randint(0, 2)):
                inter.agregar_vehiculo("NS")
            for _ in range(random.randint(0, 2)):
                inter.agregar_vehiculo("EW")

    def paso(self):
        """Ejecuta un paso completo de la simulación."""
        print(f"--- Paso {self.tiempo} ---")
        self.agregar_vehiculos()  # Añade nuevos vehículos a las intersecciones
        
        # Actualiza el estado de vehículos y semáforos en cada intersección
        for inter in self.intersecciones:
            inter.actualizar_vehiculos()      
            inter.actualizar_semaforos()     
            inter.imprimir_estado()          
            
        self.tiempo += 1  