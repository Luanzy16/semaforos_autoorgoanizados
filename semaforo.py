class Semaforo:
    def __init__(self, direccion, tiempo_minimo=3, max_rojo=8):
        self.direccion = direccion  #"NS" o "EW" - Dirección que controla el semáforo
        self.estado = "rojo" #Todos los semáforos inician en rojo
        self.tiempo_verde_actual = 0 #Contador de tiempo en estado verde
        self.tiempo_rojo = 0 #Contador de tiempo en estado rojo

        # Parámetros de reglas
        self.tiempo_minimo = tiempo_minimo #REGLA 2: Tiempo mínimo que debe permanecer en verde (u)
        self.max_rojo = max_rojo #Tiempo máximo permitido en rojo antes de forzar cambio

    def poner_verde(self):
        #Cambia el semáforo a verde y reinicia contadores
        self.estado = "verde"
        self.tiempo_verde_actual = 0 #Reinicia contador de tiempo en verde
        self.tiempo_rojo = 0 #Reinicia contador de tiempo en rojo

    def poner_rojo(self):
        #Cambia el semáforo a rojo y reinicia contadores
        self.estado = "rojo"
        self.tiempo_verde_actual = 0 #Reinicia contador de tiempo en verde
        self.tiempo_rojo = 0 #Reinicia contador de tiempo en rojo

    def actualizar(self, en_verde):
        """
        Actualiza contadores según el estado actual del semáforo.
        
        Args:
            en_verde (bool): Indica si este semáforo está actualmente en verde.
                             Esto ayuda a determinar qué contador actualizar.
        """
        if self.estado == "verde":
            self.tiempo_verde_actual += 1 #Incrementa tiempo en verde (para REGLA 2)
        else:
            self.tiempo_rojo += 1 #Incrementa tiempo en rojo (para evitar esperas prolongadas)
