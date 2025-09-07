from simulacion import Simulacion
import time

sim = Simulacion()

# Simular 10 pasos
for _ in range(10):
    sim.paso()
    time.sleep(1)  # esperar 1 segundo para ver la salida paso a paso
