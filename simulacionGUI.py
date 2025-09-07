import pygame
import sys

# ===================================
# Clase GUI para conectar con Simulacion
# ===================================
class SimulacionGUI:
    def __init__(self, simulacion, ancho=600, alto=600):
        self.simulacion = simulacion
        self.ancho = ancho
        self.alto = alto
        self.ventana = None
        self.reloj = None
        self.escala = 100  # tamaño por intersección

        # Inicializar pygame
        pygame.init()
        self.ventana = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Simulación de Tráfico")
        self.reloj = pygame.time.Clock()

    def dibujar_calles(self):
        gris = (50, 50, 50)
        for i in range(1, self.simulacion.tamano):
            # Líneas horizontales
            pygame.draw.rect(self.ventana, gris, (0, i*self.escala-20, self.ancho, 40))
            # Líneas verticales
            pygame.draw.rect(self.ventana, gris, (i*self.escala-20, 0, 40, self.alto))

    def dibujar_semaforos(self):
        for i in range(self.simulacion.tamano):
            for j in range(self.simulacion.tamano):
                inter = self.simulacion.intersecciones[i][j]
                color = (0,255,0) if inter.semaforo.estado == "verde" else (255,0,0)
                pygame.draw.circle(self.ventana, color,
                                   (j*self.escala + self.escala//2, i*self.escala + self.escala//2),
                                   10)

    def dibujar_vehiculos(self):
        azul = (0,0,255)
        for v in self.simulacion.vehiculos:
            # Rectángulo que representa el auto
            pygame.draw.rect(self.ventana, azul, (v.x, v.y, 15, 10))

    def actualizar_vehiculos_posicion(self):
        for v in self.simulacion.vehiculos:
            if v.posicion:  # Está en alguna intersección
                i, j = v.posicion
                inter = self.simulacion.intersecciones[i][j]

                # Coordenadas base de la intersección
                base_x = j * self.escala + self.escala//2
                base_y = i * self.escala + self.escala//2

                # Si no tiene coordenadas gráficas aún, asignarlas
                if v.x is None or v.y is None:
                    v.x, v.y = base_x, base_y

                # Movimiento según dirección y semáforo
                if v.direccion == "E":
                    if inter.semaforo.estado == "verde":
                        v.x += 2
                elif v.direccion == "W":
                    if inter.semaforo.estado == "verde":
                        v.x -= 2
                elif v.direccion == "S":
                    if inter.semaforo.estado == "verde":
                        v.y += 2
                elif v.direccion == "N":
                    if inter.semaforo.estado == "verde":
                        v.y -= 2


    def ejecutar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Paso de la simulación lógica
            self.simulacion.paso()

            # Actualizar posiciones gráficas
            self.actualizar_vehiculos_posicion()

            # Dibujar
            self.ventana.fill((200,200,200))
            self.dibujar_calles()
            self.dibujar_semaforos()
            self.dibujar_vehiculos()

            pygame.display.flip()
            self.reloj.tick(10)  # 10 FPS
