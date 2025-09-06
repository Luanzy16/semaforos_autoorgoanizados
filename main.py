from interseccion import Interseccion

# Crear intersección
inter = Interseccion()

# Agregar autos iniciales
for _ in range(5):
    inter.agregar_vehiculo("N")
    inter.agregar_vehiculo("E")

# Simulación
for t in range(20):
    print(f"\nTiempo {t}")
    inter.paso()
    print(inter.estado())
