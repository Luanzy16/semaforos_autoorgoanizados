from simulacion import Simulacion
import time #Importa el módulo time para controlar pausas

sim = Simulacion() #Instancia de la simulación

# Simular 10 pasos
for _ in range(10):
    sim.paso() #Ejecuta un paso de la simulación
    time.sleep(1)  #Esperar 1 segundo para ver la salida paso a paso