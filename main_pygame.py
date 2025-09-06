import pygame
import random
from interseccion import Interseccion

# Inicializar pygame
pygame.init()
ANCHO, ALTO = 600, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Semáforos Autoorganizantes")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (200, 0, 0)
VERDE = (0, 200, 0)
AZUL = (0, 0, 200)

# Escala de posiciones
ESCALA = 20  # cada unidad = 20 px

# Dibujar semáforos
def dibujar_semaforos(inter):
    # Norte
    color_N = VERDE if inter.semaforos["N"].verde else ROJO
    pygame.draw.circle(VENTANA, color_N, (ANCHO//2, ALTO//2 - 100), 20)
    # Este
    color_E = VERDE if inter.semaforos["E"].verde else ROJO
    pygame.draw.circle(VENTANA, color_E, (ANCHO//2 + 100, ALTO//2), 20)

# Dibujar vehículos
def dibujar_autos(inter):
    for v in inter.vehiculos:
        if v.direccion == "N":
            x = ANCHO//2 - 40
            y = ALTO//2 - v.posicion * ESCALA
        else:  # Este
            x = ANCHO//2 + v.posicion * ESCALA
            y = ALTO//2 + 40
        color = AZUL if not v.detenido else ROJO
        pygame.draw.rect(VENTANA, color, (x, y, 20, 20))

def main():
    reloj = pygame.time.Clock()
    inter = Interseccion()

    # autos iniciales
    for _ in range(3):
        inter.agregar_vehiculo("N")
        inter.agregar_vehiculo("E")

    corriendo = True
    paso = 0

    while corriendo:
        reloj.tick(2)  # 2 pasos por segundo
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # cada 4 pasos, agregar un auto
        if paso % 4 == 0:
            if random.random() < 0.5:
                inter.agregar_vehiculo("N")
            else:
                inter.agregar_vehiculo("E")

        # avanzar simulación
        inter.paso()

        # dibujar
        VENTANA.fill(NEGRO)

        # calles
        pygame.draw.rect(VENTANA, BLANCO, (ANCHO//2 - 60, 0, 120, ALTO))  # vertical
        pygame.draw.rect(VENTANA, BLANCO, (0, ALTO//2 - 60, ANCHO, 120))  # horizontal

        dibujar_semaforos(inter)
        dibujar_autos(inter)

        pygame.display.update()
        paso += 1

    pygame.quit()

if __name__ == "__main__":
    main()
