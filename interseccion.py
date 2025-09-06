from vehiculo import Vehiculo
from semaforo import Semaforo
import random

class Interseccion:
    def __init__(self, umbral_n=3, dist_d=5, dist_r=2, dist_e=2, m=2, u=5):
        self.semaforos = {
            "N": Semaforo("N", verde=True, u=u),
            "E": Semaforo("E", verde=False, u=u)
        }
        self.vehiculos = []
        self.param = dict(umbral_n=umbral_n, dist_d=dist_d, dist_r=dist_r,
                          dist_e=dist_e, m=m, u=u)

    def agregar_vehiculo(self, direccion):
        """Crea un vehículo a una distancia aleatoria."""
        self.vehiculos.append(Vehiculo(posicion=random.randint(6, 10), direccion=direccion))

    def aplicar_reglas(self):
        N, E = self.semaforos["N"], self.semaforos["E"]
        p = self.param

        # ---- Regla 1: contador en rojo ----
        for v in self.vehiculos:
            sem = self.semaforos[v.direccion]
            if not sem.verde and v.posicion <= p["dist_d"]:
                sem.contador += 1

        for s in self.semaforos.values():
            if s.contador >= p["umbral_n"] and s.tiempo_verde >= p["u"]:
                self._cambiar_semaforo(s.direccion)

        # ---- Regla 3: pocos vehículos cruzando ----
        for s in self.semaforos.values():
            if s.verde:
                cerca = sum(1 for v in self.vehiculos if v.direccion == s.direccion and v.posicion <= p["dist_r"])
                if 0 < cerca <= p["m"]:
                    return  # no cambiar aún

        # ---- Regla 4: bloqueo adelante ----
        for s in self.semaforos.values():
            if s.verde:
                bloqueado = any(v.direccion == s.direccion and v.posicion < 0 and v.detenido for v in self.vehiculos)
                if bloqueado and s.tiempo_verde >= p["u"]:
                    self._cambiar_semaforo(s.direccion)

        # ---- Regla 6: bloqueo en ambas direcciones ----
        bloqueado_N = any(v.direccion == "N" and v.posicion < 0 and v.detenido for v in self.vehiculos)
        bloqueado_E = any(v.direccion == "E" and v.posicion < 0 and v.detenido for v in self.vehiculos)

        if bloqueado_N and bloqueado_E:
            N.cambiar(False)
            E.cambiar(False)
        elif bloqueado_N and not bloqueado_E:
            E.cambiar(True)
            N.cambiar(False)
        elif bloqueado_E and not bloqueado_N:
            N.cambiar(True)
            E.cambiar(False)

    def _cambiar_semaforo(self, direccion):
        """Cambia el semáforo de una dirección y sincroniza el opuesto."""
        actual = self.semaforos[direccion]
        opuesto = self.semaforos["E"] if direccion == "N" else self.semaforos["N"]
        actual.cambiar(False)
        opuesto.cambiar(True)

    def paso(self):
        """Avanza un paso de simulación."""
        # avanzar semáforos
        for s in self.semaforos.values():
            s.paso()

        # mover vehículos
        for v in self.vehiculos:
            sem = self.semaforos[v.direccion]
            if v.posicion == 0:
                if sem.verde:
                    v.mover()  # cruza
                else:
                    v.detenido = True
            else:
                v.mover()

        # aplicar reglas
        self.aplicar_reglas()

    def estado(self):
        """Devuelve el estado actual de la intersección."""
        return {
            "Semaforos": {d: ("Verde" if s.verde else "Rojo") for d, s in self.semaforos.items()},
            "Vehiculos": [(v.direccion, v.posicion, "Detenido" if v.detenido else "Moviendo") for v in self.vehiculos]
        }
