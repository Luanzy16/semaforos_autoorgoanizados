class SemaforoConvencional:
    def __init__(self, direccion, tiempo_verde=15, tiempo_rojo=15):
        self.direccion = direccion
        self.estado = "rojo"
        self.tiempo_verde = tiempo_verde
        self.tiempo_rojo = tiempo_rojo
        self.contador_tiempo = 0
        
    def actualizar(self):
        self.contador_tiempo += 1
        if self.estado == "verde" and self.contador_tiempo >= self.tiempo_verde:
            self.estado = "rojo"
            self.contador_tiempo = 0
        elif self.estado == "rojo" and self.contador_tiempo >= self.tiempo_rojo:
            self.estado = "verde"
            self.contador_tiempo = 0
    
    def poner_verde(self):
        self.estado = "verde"
        self.contador_tiempo = 0
        
    def poner_rojo(self):
        self.estado = "rojo"
        self.contador_tiempo = 0