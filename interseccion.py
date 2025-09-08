import random
from semaforo import Semaforo
from vehiculo import Vehiculo

class Interseccion:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion  # (x,y) en canvas

        # Semáforos
        self.semaforo_NS = Semaforo("NS")
        self.semaforo_EW = Semaforo("EW")
        self.semaforo_NS.poner_verde()  # inicia NS en verde

        # Colas de vehículos
        self.cola_NS = []
        self.cola_EW = []

        # Reglas
        self.max_cola = 5

    def agregar_vehiculo(self, direccion):
        if direccion == "NS":
            self.cola_NS.append(Vehiculo("NS"))
        elif direccion == "EW":
            self.cola_EW.append(Vehiculo("EW"))

    def actualizar_semaforos(self):
        """Aplica las reglas autoorganizadas."""
        # Actualizar contadores
        self.semaforo_NS.actualizar(self.semaforo_NS.estado == "verde")
        self.semaforo_EW.actualizar(self.semaforo_EW.estado == "verde")

        if self.semaforo_NS.estado == "verde":
            # Condiciones para cambiar a EW
            if self.semaforo_NS.tiempo_verde_actual >= self.semaforo_NS.tiempo_minimo:
                if len(self.cola_EW) >= self.max_cola or self.semaforo_EW.tiempo_rojo >= self.semaforo_EW.max_rojo:
                    self.semaforo_NS.poner_rojo()
                    self.semaforo_EW.poner_verde()

        elif self.semaforo_EW.estado == "verde":
            # Condiciones para cambiar a NS
            if self.semaforo_EW.tiempo_verde_actual >= self.semaforo_EW.tiempo_minimo:
                if len(self.cola_NS) >= self.max_cola or self.semaforo_NS.tiempo_rojo >= self.semaforo_NS.max_rojo:
                    self.semaforo_EW.poner_rojo()
                    self.semaforo_NS.poner_verde()

    def actualizar_vehiculos_logica(self):
        """Avanza un vehículo si su semáforo está en verde."""
        if self.semaforo_NS.estado == "verde" and self.cola_NS:
            self.cola_NS.pop(0)
        if self.semaforo_EW.estado == "verde" and self.cola_EW:
            self.cola_EW.pop(0)

    def actualizar_vehiculos_visual(self):
        """(placeholder) Movimiento animado."""
        for v in self.cola_NS + self.cola_EW:
            v.mover()

    def dibujar_en_canvas(self, canvas, ancho_calle):
        """Dibuja semáforos en el canvas."""
        x, y = self.posicion
        r = 10
        # NS
        color_ns = "green" if self.semaforo_NS.estado == "verde" else "red"
        canvas.create_oval(x-r, y-40-r, x+r, y-40+r, fill=color_ns, tags="semaforo")
        # EW
        color_ew = "green" if self.semaforo_EW.estado == "verde" else "red"
        canvas.create_oval(x+40-r, y-r, x+40+r, y+r, fill=color_ew, tags="semaforo")

    def dibujar_vehiculos_en_canvas(self, canvas, ancho_calle):
        x, y = self.posicion
        size = 8
        # NS
        for i, _ in enumerate(self.cola_NS):
            canvas.create_rectangle(x-10, y-60-(i*12), x+10, y-50-(i*12), fill="blue", tags="vehiculo")
        # EW
        for i, _ in enumerate(self.cola_EW):
            canvas.create_rectangle(x+60+(i*12), y-10, x+70+(i*12), y+10, fill="yellow", tags="vehiculo")

    def imprimir_estado(self):
        print(f"Intersección {self.nombre}: "
              f"NS({self.semaforo_NS.estado}, {len(self.cola_NS)} autos), "
              f"EW({self.semaforo_EW.estado}, {len(self.cola_EW)} autos))")
