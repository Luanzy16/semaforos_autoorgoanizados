import random
from vehiculo import Vehiculo
from semaforo_convencional import SemaforoConvencional

class InterseccionConvencional:
    def __init__(self, nombre, posicion, tiempo_verde_ns=15, tiempo_verde_ew=15):
        self.nombre = nombre
        self.posicion = posicion
        
        self.semaforo_NS = SemaforoConvencional("NS", tiempo_verde_ns, tiempo_verde_ew)
        self.semaforo_EW = SemaforoConvencional("EW", tiempo_verde_ew, tiempo_verde_ns)
        self.semaforo_NS.poner_verde()
        
        self.cola_NS = []
        self.cola_EW = []
        
    def agregar_vehiculo(self, direccion):
        if direccion == "NS":
            self.cola_NS.append(Vehiculo("NS"))
        elif direccion == "EW":
            self.cola_EW.append(Vehiculo("EW"))
    
    def actualizar_semaforos(self):
        self.semaforo_NS.actualizar()
        self.semaforo_EW.actualizar()
    
    def actualizar_vehiculos_logica(self):
        if self.semaforo_NS.estado == "verde" and self.cola_NS:
            self.cola_NS.pop(0)
        if self.semaforo_EW.estado == "verde" and self.cola_EW:
            self.cola_EW.pop(0)
    
    def actualizar_vehiculos_visual(self):
        for v in self.cola_NS + self.cola_EW:
            v.mover()
    
    def dibujar_en_canvas(self, canvas, ancho_calle):
        x, y = self.posicion
        r = 10
        color_ns = "green" if self.semaforo_NS.estado == "verde" else "red"
        color_ew = "green" if self.semaforo_EW.estado == "verde" else "red"
        
        canvas.create_oval(x-r, y-40-r, x+r, y-40+r, fill=color_ns, tags="semaforo")
        canvas.create_oval(x+40-r, y-r, x+40+r, y+r, fill=color_ew, tags="semaforo")
    
    def dibujar_vehiculos_en_canvas(self, canvas, ancho_calle):
        x, y = self.posicion
        size = 8
        
        for i, _ in enumerate(self.cola_NS):
            canvas.create_rectangle(x-10, y-60-(i*12), x+10, y-50-(i*12), fill="blue", tags="vehiculo")
        for i, _ in enumerate(self.cola_EW):
            canvas.create_rectangle(x+60+(i*12), y-10, x+70+(i*12), y+10, fill="yellow", tags="vehiculo")
    
    def imprimir_estado(self):
        print(f"Intersección {self.nombre}: "
              f"NS({self.semaforo_NS.estado}, {len(self.cola_NS)} autos), "
              f"EW({self.semaforo_EW.estado}, {len(self.cola_EW)} autos)")