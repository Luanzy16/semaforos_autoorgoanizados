# Simulación de Semáforos Autoorganizados

Integrantes

 - Luis Sanchez
 - Valentina Andrade
 - Mateo Patiño

## 📘 Descripción General
Este proyecto implementa una **simulación de semáforos autoorganizados** en un cruce vial.  
El objetivo es modelar cómo los semáforos pueden **ajustar sus estados de manera autónoma** en función del tráfico real, sin necesidad de un controlador central o un plan fijo de tiempos.

El sistema utiliza reglas locales inspiradas en modelos de tráfico autoorganizado para mejorar la fluidez y evitar atascos.

---

## 🔹 Semáforos simulados
- Se simulan **2 semáforos principales**:
  1. **Semáforo NS (Norte-Sur)**
  2. **Semáforo EW (Este-Oeste)**

Cada semáforo controla el flujo de vehículos en su dirección.  
El estado de ambos está **interconectado**: cuando uno está en verde, el otro está en rojo.

---

## 🔹 Secuencia de colores
Cada semáforo puede estar en los siguientes estados:

1. **Rojo** → Detiene el tráfico.  
2. **Verde** → Permite el paso de vehículos.  

---

## 🔹 Reglas de Autoorganización
El sistema se rige por **cinco reglas locales** que determinan cuándo cambiar los semáforos:

### 1️⃣ Acumulación de vehículos en rojo
- Cada paso de tiempo se suma al contador de vehículos detenidos frente a una luz roja (dentro de una distancia `d`).  
- Si el contador excede un umbral `n`, el semáforo cambia a verde.  
- Al cambiar, el contador se reinicia.

### 2️⃣ Tiempo mínimo en verde
- Un semáforo debe permanecer al menos `u` segundos en verde antes de poder volver a cambiar.  
- Esto evita cambios demasiado rápidos e ineficientes.

### 3️⃣ Mantener verde si pocos vehículos están cruzando
- Si `m` o menos vehículos están cruzando con la luz verde (dentro de una distancia `r`), el semáforo no cambia a rojo.  
- Se espera a que crucen antes de decidir el cambio.

### 4️⃣ Detección de bloqueo más allá de la intersección
- Si un vehículo está detenido a una distancia `e` después de la intersección, el semáforo se pone en rojo.  
- Esto evita que los autos queden atascados bloqueando el cruce.

### 5️⃣ Bloqueo en ambas direcciones
- Si hay vehículos detenidos en ambas direcciones más allá de la intersección, se ponen ambas luces en rojo.  
- Cuando una dirección se libera, el verde se restaura automáticamente en esa vía.

---

## 🔹 Comunicación entre semáforos
Los semáforos **no tienen un controlador central**, sino que se comunican de manera **implícita** mediante:

- **Reglas compartidas** (misma lógica en cada semáforo).  
- **Detección de estados de vehículos** (esperando, cruzando o bloqueados).  
- **Interdependencia**: cuando uno cambia a verde, el otro cambia a rojo.

De esta forma, el orden global del tráfico **emerge** del comportamiento local de cada semáforo.

---

## 🔹 Flujo de la simulación
1. Se generan vehículos en las direcciones **NS** y **EW**.  
2. Los vehículos avanzan hasta la intersección y se detienen si la luz está en rojo.  
3. En cada paso de tiempo:
   - Los semáforos aplican las reglas y actualizan su estado.  
   - Los vehículos avanzan o esperan según el semáforo.  
4. El sistema evoluciona mostrando cómo los semáforos se autoorganizan.

---

## 🔹 Conclusión
Este modelo representa un sistema **autoorganizado** de control de tráfico porque:
- Las decisiones se toman en base a condiciones locales.  
- No existe sincronización externa ni plan rígido.  
- El flujo ordenado de vehículos **emerge** del comportamiento colectivo.

---

## ⚙️ Parámetros ajustables
- `d` → Distancia de detección de vehículos en rojo.  
- `n` → Umbral de vehículos acumulados para cambiar a verde.  
- `u` → Tiempo mínimo en verde antes de poder cambiar.  
- `m` → Cantidad mínima de vehículos cruzando antes de permitir cambio.  
- `r` → Distancia de detección de vehículos cruzando.  
- `e` → Distancia de detección de bloqueo después de la intersección.  

---

# Como ejecutarlo 

## 📋 Requisitos

- Python **3.8+**
- Librerías estándar (no necesitas instalar nada extra):
  - `tkinter` (viene incluido con Python en la mayoría de distribuciones)

---


 Abre una terminal dentro de la carpeta del proyecto y ejecuta:

```bash
python simulacionGUI.py
