import random
import tkinter as tk
from interseccion import Interseccion

class Simulacion:
    def __init__(self, master):
        self.master = master #Ventana principal del Tkinter
        master.title("Simulador de Semaforos Autoorganizados")

        self.simulacion_activa = False #Controla si la simulación esta activa
        self.ancho_calle = 80 

        #Posiciones de las intersecciones en el canvas (coordenadas x, y)
        self.posiciones = {
            "A": (200, 200),
            "B": (600, 200),
            "C": (200, 400),
            "D": (600, 400),
        }

        #Creacion de las 4 intersecciones del sistema
        self.intersecciones = [
            Interseccion("A", self.posiciones["A"]),
            Interseccion("B", self.posiciones["B"]),
            Interseccion("C", self.posiciones["C"]),
            Interseccion("D", self.posiciones["D"])
        ]

        self.tiempo = 0 #Contador de pasos de la simulación

        self.canvas = tk.Canvas(master, width=800, height=600, bg="darkgreen")
        self.canvas.pack() #Poner el canvas en la ventana emergente
        self.dibujar_escena() #Dibujar la escena inicial

        #Frame para los botones de control
        frame_botones = tk.Frame(master)
        frame_botones.pack()

        #Boton para iniciar simulación
        self.boton_iniciar = tk.Button(frame_botones, text="Iniciar", command=self.iniciar_simulacion)
        self.boton_iniciar.pack(side=tk.LEFT, padx=10)

        #Boton para detener la simulación
        self.boton_detener = tk.Button(frame_botones, text="Detener", command=self.detener_simulacion)
        self.boton_detener.pack(side=tk.LEFT, padx=10)

    def dibujar_escena(self):
        #Dibuja la escena estática del sistema vial
        color_calle = "#808080"
        color_linea = "#FFFFFF" #Lineas de división

        #Calles Verticales
        self.canvas.create_rectangle(200-40, 0, 200+40, 600, fill=color_calle, outline="") #Calle como rectangulo
        self.canvas.create_rectangle(600-40, 0, 600+40, 600, fill=color_calle, outline="")
        self.canvas.create_line(200, 0, 200, 600, fill=color_linea, dash=(5,5)) #Linea punteada para divisiones
        self.canvas.create_line(600, 0, 600, 600, fill=color_linea, dash=(5,5))

        #Calles Horizontales
        self.canvas.create_rectangle(0, 200-40, 800, 200+40, fill=color_calle, outline="")
        self.canvas.create_rectangle(0, 400-40, 800, 400+40, fill=color_calle, outline="")
        self.canvas.create_line(0, 200, 800, 200, fill=color_linea, dash=(5,5))
        self.canvas.create_line(0, 400, 800, 400, fill=color_linea, dash=(5,5))

        #Dibujar todas las intersecciones en el canvas
        for inter in self.intersecciones:
            inter.dibujar_en_canvas(self.canvas, self.ancho_calle)

    def actualizar_visualizacion(self):
        #Actualiza la visualización de vehículos y semáforos.
        #Eliminar elementos antiguos para evitar superposición
        self.canvas.delete("vehiculo") #Elimina todos los vehículos
        self.canvas.delete("semaforo") #Elimina todos los semáforos

        #Dibujar nuevamente todos los elementos actualizados
        for inter in self.intersecciones:
            inter.dibujar_vehiculos_en_canvas(self.canvas, self.ancho_calle)
            inter.dibujar_en_canvas(self.canvas, self.ancho_calle)

    def animacion_loop(self): #Bucle principal de animación que se ejecuta cada 50ms
        if self.simulacion_activa:
            #Actualiza posición visual de vehículos en todas las intersecciones
            for inter in self.intersecciones:
                inter.actualizar_vehiculos_visual()
            #Actualiza la visualización completa
            self.actualizar_visualizacion()
            #Programa el próximo frame de animación (50ms = 20 FPS)
            self.master.after(50, self.animacion_loop)

    def agregar_vehiculos(self):
        #Agrega vehículos aleatoriamente a las intersecciones.
        if self.simulacion_activa:
            for inter in self.intersecciones:
                #40% de probabilidad de agregar vehículo en dirección Norte-Sur
                if random.random() < 0.4:
                    inter.agregar_vehiculo("NS")
                #40% de probabilidad de agregar vehículo en dirección Este-Oeste
                if random.random() < 0.4:
                    inter.agregar_vehiculo("EW")

    def simulacion_paso(self):
        #Ejecuta un paso completo de la simulación lógica.
        #Este método se ejecuta cada 2 segundos ya agrega nuevos vehiculos, actualiza vehiculos y semaforos
        if self.simulacion_activa:
            print(f"--- Paso {self.tiempo} ---")#Encabezado del paso actual
            #Agregar vehículos aleatoriamente
            self.agregar_vehiculos()
            #Procesar todas las intersecciones
            for inter in self.intersecciones:
                inter.actualizar_vehiculos_logica() #Actualizar la logica de los vehiculos
                inter.actualizar_semaforos() #Actualizar los semaforos
                inter.imprimir_estado() #Mostrar estado en la consola
            self.tiempo += 1 #Incrementar contador de tiempo
             #Programar el próximo paso de simulación (2 segundos)
            self.master.after(2000, self.simulacion_paso)

    def iniciar_simulacion(self):
        #Activa ambos bucles: lógico (cada 2s) y de animación (cada 50ms)
        if not self.simulacion_activa:
            self.simulacion_activa = True #Activar simulación
            self.simulacion_paso() #Iniciar bucle lógico
            self.animacion_loop() #Iniciar bucle de animación

    def detener_simulacion(self):
        #Detiene la simulación estableciendo la bandera en False para la próxima iteración
        self.simulacion_activa = False

#Punto de entrada del programa
if __name__ == "__main__":
    root = tk.Tk() #Ventana principal de Tkinter
    sim = Simulacion(root) #Instancia de la simulación
    root.mainloop() #Inicia el bucle principal de Tkinter