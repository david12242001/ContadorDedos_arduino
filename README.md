#  Miniproyecto 2: Contador de Dedos con Python y Arduino video demostrativo al final

Este proyecto consiste en un sistema de visión por computadora que detecta cuántos dedos tiene levantados una persona (de 0 a 5) usando la cámara web y, a través de comunicación serial, envía ese valor a una placa Arduino. El Arduino simula una suma acumulativa o muestra el conteo en un circuito electrónico, utilizando LEDs o un display.

---

## Objetivo

Desarrollar un contador de dedos en tiempo real, combinando visión artificial en Python con MediaPipe y OpenCV, y hardware controlado por Arduino para visualizar el conteo.

---

## ¿Cómo funciona?

1. **Captura de video en tiempo real:** se utiliza la cámara del computador mediante OpenCV.
2. **Detección de dedos:** el modelo de MediaPipe detecta la mano y analiza la posición de los dedos para determinar cuántos están levantados.
3. **Envío al Arduino:** cuando se detecta un cambio en el número de dedos, se envía ese número por el puerto serial usando `pyserial`.
4. **Visualización física:** en Arduino, se actualiza un conjunto de LEDs, un display de 7 segmentos o un LCD para mostrar el número recibido.

---

## componentes usados

### 🔹 Software

- Python 3.x
- OpenCV (`pip install opencv-python`)
- MediaPipe (`pip install mediapipe`)
- PySerial (`pip install pyserial`)
- Arduino IDE

### 🔹 Hardware

- Placa Arduino UNO
- Protoboard
- Cables jumper
- Resistencias
- display de 7 segmentos

## funcionamiento
- Se ejecuta contador_dedos.py, que abre la cámara y detecta los dedos.
- Cuando cambia el número detectado, se manda al Arduino por USB.
- El Arduino recibe el número y enciende los LEDs o muestra el valor.

## explicacion de codigo phyton y arduino
## phyton
(contador_dedos.py)
El script en Python utiliza MediaPipe y OpenCV para detectar la mano en tiempo real mediante la cámara web. Se identifica si los dedos están levantados comparando las coordenadas de sus puntos clave. El número de dedos levantados se muestra en pantalla y se envía al Arduino a través del puerto serial COM4, usando la librería pyserial.

Funciones destacadas:

contar_dedos(): Evalúa si cada dedo está levantado según su posición respecto a sus articulaciones.

arduino.write(): Envía el número de dedos al Arduino convertido en texto.

## Arduino (arduino_display.ino)
El Arduino recibe los datos enviados desde Python y los usa para mostrar el número de dedos levantados en un display de 7 segmentos. Se usan 7 pines digitales (2 al 8) para controlar cada segmento del display.

🔧 Funciones destacadas:

mostrarNumero(int n): Enciende los segmentos necesarios para mostrar el número recibido (de 0 a 5).

El código solo acepta números entre '0' y '5' para evitar errores en el display.





## 🎥 Video demostrativo
Puedes ver el video demostrativo.
[Ver video] https://drive.google.com/file/d/1mlnZgP_ahkePfmTaHPObxLUPPSLsVJmw/view?usp=sharing
