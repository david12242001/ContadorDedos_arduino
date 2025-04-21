import cv2
import mediapipe as mp
import serial
import time

# Configuración del puerto serial con Arduino
arduino = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,  # Solo una mano para evitar confusión
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)
mp_drawing = mp.solutions.drawing_utils

# Función para contar dedos con mejor precisión
def contar_dedos(hand_landmarks):
    dedos = 0

    # Obtener landmarks de referencia más fácil
    lm = hand_landmarks.landmark

    # Pulgar (compara eje X por posición lateral)
    if lm[mp_hands.HandLandmark.THUMB_TIP].x < lm[mp_hands.HandLandmark.THUMB_IP].x:
        dedos += 1

    # Índice
    if lm[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < lm[mp_hands.HandLandmark.INDEX_FINGER_PIP].y:
        dedos += 1

    # Medio
    if lm[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < lm[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y:
        dedos += 1

    # Anular
    if lm[mp_hands.HandLandmark.RING_FINGER_TIP].y < lm[mp_hands.HandLandmark.RING_FINGER_PIP].y:
        dedos += 1

    # Meñique
    if lm[mp_hands.HandLandmark.PINKY_TIP].y < lm[mp_hands.HandLandmark.PINKY_PIP].y:
        dedos += 1

    return dedos

# Activar cámara
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Espejar imagen y convertir a RGB
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Dibujar mano
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Contar dedos
            dedos = contar_dedos(hand_landmarks)
            cv2.putText(frame, f'Dedos: {dedos}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Enviar valor al Arduino
            arduino.write(str(dedos).encode())

    # Mostrar resultado
    cv2.imshow('Contador de Dedos', frame)

    # Salir con ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
