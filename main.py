import cv2
import mediapipe as mp
import numpy as np
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
selected_color = colors[0]

prev_x, prev_y = None, None
canvas = np.zeros((1080, 1920, 3), dtype=np.uint8)

def select_color(x, y):
    global selected_color
    if 50 < y < 100:
        if 50 < x < 100:
            selected_color = colors[0]
        elif 150 < x < 200:
            selected_color = colors[1]
        elif 250 < x < 300:
            selected_color = colors[2]
        elif 350 < x < 400:
            selected_color = colors[3]

def are_thumb_and_index_separated(hand_landmarks, min_distance=0.3):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    distance = math.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2)
    return distance > min_distance

def clear_canvas(x, y):
    global canvas
    if 50 < y < 100 and 450 < x < 550:
        canvas = np.zeros_like(canvas)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    if canvas.shape != frame.shape:
        canvas = np.zeros_like(frame)

    result = hands.process(rgb_frame)
    
    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1])
        y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0])
        
        if are_thumb_and_index_separated(hand_landmarks):
            if prev_x is not None and prev_y is not None:
                cv2.line(canvas, (prev_x, prev_y), (x, y), selected_color, thickness=10)
            prev_x, prev_y = x, y
        else:
            prev_x, prev_y = None, None

        select_color(x, y)
        clear_canvas(x, y)
    else:
        prev_x, prev_y = None, None

    cv2.rectangle(frame, (50, 50), (100, 100), colors[0], -1)
    cv2.rectangle(frame, (150, 50), (200, 100), colors[1], -1)
    cv2.rectangle(frame, (250, 50), (300, 100), colors[2], -1)
    cv2.rectangle(frame, (350, 50), (400, 100), colors[3], -1)
    
    cv2.rectangle(frame, (450, 50), (600, 100), (255, 255, 255), -1)
    cv2.putText(frame, 'Borrar', (460, 85), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    
    frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

    cv2.imshow('Prueba cracks', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()