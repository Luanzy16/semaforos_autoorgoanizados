import random
import tkinter as tk
from interseccion import Interseccion

class Simulacion:
    def __init__(self, master):
        self.master = master
        master.title("Simulador de Semaforos Autoorganizados")

        self.simulacion_activa = False
        self.ancho_calle = 80

        self.posiciones = {
            "A": (200, 200),
            "B": (600, 200),
            "C": (200, 400),
            "D": (600, 400),
        }

        self.intersecciones = [
            Interseccion("A", self.posiciones["A"]),
            Interseccion("B", self.posiciones["B"]),
            Interseccion("C", self.posiciones["C"]),
            Interseccion("D", self.posiciones["D"])
        ]

        self.tiempo = 0

        self.canvas = tk.Canvas(master, width=800, height=600, bg="darkgreen")
        self.canvas.pack()
        self.dibujar_escena()

        frame_botones = tk.Frame(master)
        frame_botones.pack()

        self.boton_iniciar = tk.Button(frame_botones, text="Iniciar", command=self.iniciar_simulacion)
        self.boton_iniciar.pack(side=tk.LEFT, padx=10)

        self.boton_detener = tk.Button(frame_botones, text="Detener", command=self.detener_simulacion)
        self.boton_detener.pack(side=tk.LEFT, padx=10)

    def dibujar_escena(self):
        color_calle = "#808080"
        color_linea = "#FFFFFF"

        # Verticales
        self.canvas.create_rectangle(200-40, 0, 200+40, 600, fill=color_calle, outline="")
        self.canvas.create_rectangle(600-40, 0, 600+40, 600, fill=color_calle, outline="")
        self.canvas.create_line(200, 0, 200, 600, fill=color_linea, dash=(5,5))
        self.canvas.create_line(600, 0, 600, 600, fill=color_linea, dash=(5,5))

        # Horizontales
        self.canvas.create_rectangle(0, 200-40, 800, 200+40, fill=color_calle, outline="")
        self.canvas.create_rectangle(0, 400-40, 800, 400+40, fill=color_calle, outline="")
        self.canvas.create_line(0, 200, 800, 200, fill=color_linea, dash=(5,5))
        self.canvas.create_line(0, 400, 800, 400, fill=color_linea, dash=(5,5))

        for inter in self.intersecciones:
            inter.dibujar_en_canvas(self.canvas, self.ancho_calle)

    def actualizar_visualizacion(self):
        self.canvas.delete("vehiculo")
        self.canvas.delete("semaforo")
        for inter in self.intersecciones:
            inter.dibujar_vehiculos_en_canvas(self.canvas, self.ancho_calle)
            inter.dibujar_en_canvas(self.canvas, self.ancho_calle)

    def animacion_loop(self):
        if self.simulacion_activa:
            for inter in self.intersecciones:
                inter.actualizar_vehiculos_visual()
            self.actualizar_visualizacion()
            self.master.after(50, self.animacion_loop)

    def agregar_vehiculos(self):
        if self.simulacion_activa:
            for inter in self.intersecciones:
                if random.random() < 0.4:
                    inter.agregar_vehiculo("NS")
                if random.random() < 0.4:
                    inter.agregar_vehiculo("EW")

    def simulacion_paso(self):
        if self.simulacion_activa:
            print(f"--- Paso {self.tiempo} ---")
            self.agregar_vehiculos()
            for inter in self.intersecciones:
                inter.actualizar_vehiculos_logica()
                inter.actualizar_semaforos()
                inter.imprimir_estado()
            self.tiempo += 1
            self.master.after(2000, self.simulacion_paso)

    def iniciar_simulacion(self):
        if not self.simulacion_activa:
            self.simulacion_activa = True
            self.simulacion_paso()
            self.animacion_loop()

    def detener_simulacion(self):
        self.simulacion_activa = False

if __name__ == "__main__":
    root = tk.Tk()
    sim = Simulacion(root)
    root.mainloop()
