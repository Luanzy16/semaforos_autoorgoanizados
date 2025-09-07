# Semáforos Autoorganizados

A continuación, se presenta la planificación completa del sistema de semáforos, detallando la lógica de funcionamiento, la secuencia de estados y las reglas de autoorganización.

---

## 1. Componentes de la Simulación

**Semaforo**:  
Representa un semáforo individual en una dirección (Norte-Sur o Este-Oeste).  
Tendrá estados de "Verde" y "Rojo". El estado "Amarillo" no se implementará para simplificar la transición.

**Interseccion**:  
Un objeto central que controla dos semáforos, uno para la dirección Norte-Sur (NS) y otro para Este-Oeste (EW).

**Vehiculo**:  
Se moverá por la intersección. Su posición y estado (detenido o en movimiento) para las transciones del semaforo.

---

## 2. Estados y Secuencia de Transición

Para evitar colisiones, la lógica de la intersección asegura que los semáforos opuestos (NS y EW) nunca estén en verde al mismo tiempo.  
El cambio de estado es directo y se basa en las reglas de autoorganización.

**Posibles cambios de estado:**

- **De Rojo a Verde**: Ocurre cuando se cumplen las reglas de autoorganización (por ejemplo, muchos vehículos esperando).  
- **De Verde a Rojo**: Ocurre cuando el tiempo mínimo en verde ha pasado y las condiciones en la dirección opuesta lo justifican.

---

## 3. Reglas de Autoorganización (Lógica Principal)

La lógica de autoorganización se implementará en el método `actualizar_semaforos()` de la clase `Interseccion`.  
En cada paso de tiempo de la simulación, la intersección revisará las siguientes reglas en el orden listado:

1. **Regla 5 (Congestión Doble)**:  
   Si hay vehículos detenidos después del cruce en ambas direcciones (NS y EW), ambos semáforos se pondrán en rojo para evitar un bloqueo total.  
   Si una de las direcciones se despeja, su semáforo podrá volver a verde.

2. **Regla 4 (Congestión Unilateral)**:  
   Si hay un vehículo detenido más allá de una luz verde en una sola dirección, esa luz cambiará a rojo.  
   Esto detendrá el flujo para permitir que el vehículo se mueva.

3. **Regla 2 (Tiempo Mínimo en Verde)**:  
   Un semáforo que acaba de cambiar a verde debe permanecer así por un tiempo mínimo (`u`).  
   Esta regla tiene prioridad sobre la de cambio por umbral de vehículos, asegurando un flujo constante.

4. **Regla 3 (Flujo Bajo)**:  
   Si una luz está en verde y hay pocos vehículos (`m` o menos) cerca de la intersección en esa dirección, no cambiará a rojo.  
   Esto evita interrupciones innecesarias en el tráfico ligero.

5. **Regla 1 (Umbral de Vehículos)**:  
   Si ninguna de las reglas anteriores aplica, la intersección revisará el número de vehículos esperando en la dirección opuesta.  
   Si este número excede un umbral (`n`), permitirá el cambio del semáforo.
