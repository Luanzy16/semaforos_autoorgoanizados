from interseccion import Interseccion
import random
import tkinter as tk
import time

class Simulacion:
    def __init__(self, master):
        self.master = master
        master.title("Simulador de Semaforos Autoorganizados")

        self.simulacion_activa = False

        self.intersecciones = [
            Interseccion("A"),
            Interseccion("B"),
            Interseccion("C"),
            Interseccion("D")
        ]
        self.tiempo = 0

        self.canvas = tk.Canvas(master, width=800, height=600, bg="darkgreen")
        self.canvas.pack()

        self.dibujar_intersecciones()

        frame_botones = tk.Frame(master)
        frame_botones.pack()

        self.boton_iniciar = tk.Button(frame_botones, text="Iniciar", command=self.iniciar_simulacion)
        self.boton_iniciar.pack(side=tk.LEFT, padx=10)

        self.boton_detener = tk.Button(frame_botones, text="Detener", command=self.detener_simulacion)
        self.boton_detener.pack(side=tk.LEFT, padx=10)

    def dibujar_intersecciones(self):
        # Coordenadas base para las 4 intersecciones
        self.posiciones = {
            "A": (200, 200),
            "B": (600, 200),
            "C": (200, 400),
            "D": (600, 400),
        }
        
        # Ancho de la calle - aumentado para mayor claridad
        ancho_calle = 80 

        # === Dibujar Calles Verticales (NS) ===
        # Carretera gris más ancha, con bordes negros
        self.canvas.create_rectangle(400 - ancho_calle/2, 0, 400 + ancho_calle/2, 600, fill="gray", outline="black", width=2)
        # Líneas de carril (blancas, punteadas)
        self.canvas.create_line(400, 0, 400, 600, fill="white", dash=(6, 6), width=2)

        # === Dibujar Calles Horizontales (EW) ===
        # Carretera gris más ancha, con bordes negros
        self.canvas.create_rectangle(0, 300 - ancho_calle/2, 800, 300 + ancho_calle/2, fill="gray", outline="black", width=2)
        # Líneas de carril (blancas, punteadas)
        self.canvas.create_line(0, 300, 800, 300, fill="white", dash=(6, 6), width=2)


        for inter in self.intersecciones:
            nombre = inter.nombre
            pos = self.posiciones[nombre]
            
            # === Dibujar el area de la interseccion (cuadrado central) ===
            # Un área de cruce más clara, ligeramente diferente al carril
            self.canvas.create_rectangle(
                pos[0] - ancho_calle/2, pos[1] - ancho_calle/2, 
                pos[0] + ancho_calle/2, pos[1] + ancho_calle/2, 
                fill="#555555", # Gris más oscuro para el centro
                outline="black", width=2
            )

            # === Dibujar las líneas de alto ===
            # Usamos un offset más pequeño para que las líneas estén justo al borde de la intersección
            offset_linea_alto = ancho_calle / 2
            
            # Para NS (arriba y abajo de la intersección)
            self.canvas.create_line(pos[0] - offset_linea_alto, pos[1] - offset_linea_alto, 
                                    pos[0] + offset_linea_alto, pos[1] - offset_linea_alto, 
                                    fill="white", width=4) # Línea norte
            self.canvas.create_line(pos[0] - offset_linea_alto, pos[1] + offset_linea_alto, 
                                    pos[0] + offset_linea_alto, pos[1] + offset_linea_alto, 
                                    fill="white", width=4) # Línea sur
            
            # Para EW (izquierda y derecha de la intersección)
            self.canvas.create_line(pos[0] - offset_linea_alto, pos[1] - offset_linea_alto, 
                                    pos[0] - offset_linea_alto, pos[1] + offset_linea_alto, 
                                    fill="white", width=4) # Línea oeste
            self.canvas.create_line(pos[0] + offset_linea_alto, pos[1] - offset_linea_alto, 
                                    pos[0] + offset_linea_alto, pos[1] + offset_linea_alto, 
                                    fill="white", width=4) # Línea este

            # Dibujar los semáforos
            self.dibujar_semaforos(inter, pos, ancho_calle)

            # Etiquetas para identificar las intersecciones
            self.canvas.create_text(pos[0], pos[1] + ancho_calle/2 + 20, text=nombre, fill="white", font=("Arial", 10, "bold"))


    def dibujar_semaforos(self, inter, pos, ancho_calle):
        # Posiciones de las luces NS y EW, ahora relativas al borde de la calle para que no se solapen
        offset_luz = ancho_calle / 2 + 10 # Un poco fuera del borde de la intersección
        
        # Semaforo NS (arriba de la intersección)
        ns_x, ns_y = pos[0], pos[1] - offset_luz
        inter.semaforo_NS.luz = self.canvas.create_oval(
            ns_x - 8, ns_y - 8, ns_x + 8, ns_y + 8, fill="red", outline="white", width=2
        )
        
        # Semaforo EW (izquierda de la intersección)
        ew_x, ew_y = pos[0] - offset_luz, pos[1]
        inter.semaforo_EW.luz = self.canvas.create_oval(
            ew_x - 8, ew_y - 8, ew_x + 8, ew_y + 8, fill="green", outline="white", width=2
        )

    def dibujar_vehiculos(self, nombre, pos):
        pass # La lógica de dibujo real está en actualizar_visualizacion
    
    def actualizar_visualizacion(self):
        self.canvas.delete("vehiculo") # Eliminar vehículos anteriores
        
        ancho_calle = 80 # Debe coincidir con el valor usado en dibujar_intersecciones
        # offset para posicionar los vehículos en carriles dentro de la calle
        offset_carril_ns = ancho_calle / 4 # Posición del carril NS (a la derecha del centro)
        offset_carril_ew = ancho_calle / 4 # Posición del carril EW (debajo del centro)
        
        for inter in self.intersecciones:
            pos_interseccion = self.posiciones[inter.nombre]
            
            # Actualizar semáforos
            color_ns = "green" if inter.semaforo_NS.estado == "Verde" else "red"
            color_ew = "green" if inter.semaforo_EW.estado == "Verde" else "red"
            
            self.canvas.itemconfig(inter.semaforo_NS.luz, fill=color_ns)
            self.canvas.itemconfig(inter.semaforo_EW.luz, fill=color_ew)

            # Dibujar vehículos NS
            for v in inter.vehiculos_NS:
                # Calculamos la posición X fija para el carril NS (a la derecha de la línea central vertical)
                x_car = pos_interseccion[0] + offset_carril_ns
                
                # Calculamos la posición Y.
                # Cuando v.posicion es pequeña, el vehículo está acercándose a la intersección (moviéndose hacia abajo en Y).
                # Cuando v.posicion es más grande, ha cruzado la intersección.
                # La intersección empieza a una distancia de 50 del centro (ancho_calle/2).
                # El centro de la intersección está en pos_interseccion[1].
                # Los vehículos se mueven hacia abajo (Y aumenta) cuando cruzan el eje EW.
                # El offset de 50 es el borde superior de la intersección.
                # v.posicion * 10 es la distancia recorrida desde su "inicio".
                y_vehiculo = pos_interseccion[1] + ancho_calle/2 - (v.posicion * 10) 
                
                self.canvas.create_rectangle(x_car - 5, y_vehiculo - 10, x_car + 5, y_vehiculo, fill="blue", tag="vehiculo")
            
            # Dibujar vehículos EW
            for v in inter.vehiculos_EW:
                # Calculamos la posición Y fija para el carril EW (debajo de la línea central horizontal)
                y_car = pos_interseccion[1] + offset_carril_ew
                
                # Calculamos la posición X.
                # Cuando v.posicion es pequeña, el vehículo está acercándose a la intersección (moviéndose hacia la izquierda en X).
                # Cuando v.posicion es más grande, ha cruzado la intersección.
                # El offset de 50 es el borde izquierdo de la intersección.
                # v.posicion * 10 es la distancia recorrida desde su "inicio".
                x_vehiculo = pos_interseccion[0] - ancho_calle/2 + (v.posicion * 10) 
                
                self.canvas.create_rectangle(x_vehiculo, y_car - 5, x_vehiculo + 10, y_car + 5, fill="red", tag="vehiculo")

    def agregar_vehiculos(self):
        for inter in self.intersecciones:
            # Controlar la aparición de vehículos para que no sea abrumadora
            if random.random() < 0.4: # 40% de probabilidad de que aparezcan vehículos
                for _ in range(random.randint(0, 2)):
                    inter.agregar_vehiculo("NS")
                for _ in range(random.randint(0, 2)):
                    inter.agregar_vehiculo("EW")

    def paso(self):
        if self.simulacion_activa:
            print(f"--- Paso {self.tiempo} ---")
            self.agregar_vehiculos()
            for inter in self.intersecciones:
                inter.actualizar_vehiculos()
                inter.actualizar_semaforos()
                inter.imprimir_estado()
            self.actualizar_visualizacion()
            self.tiempo += 1
            self.master.after(1000, self.paso)
        
    def iniciar_simulacion(self):
        self.simulacion_activa = True
        self.paso()

    def detener_simulacion(self):
        self.simulacion_activa = False

if __name__ == "__main__":
    root = tk.Tk()
    sim = Simulacion(root)
    root.mainloop()