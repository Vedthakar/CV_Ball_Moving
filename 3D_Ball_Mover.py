import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import math

# ---- config ----
pinch_thresh = 40
radius = 60
ball_angle = 0.0
angle_prev = 0.0
ball_x = 0.0
ball_y = 0.0
cx, cy = 320, 240
is_pinched = False

# ---- mediapipe ----
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.6)
mp_draw = mp.solutions.drawing_utils

# ---- camera ----
vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    ok, frame = vid.read()
    if not ok:
        continue                     # try next frame

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)

    pts = []
    if res.multi_hand_landmarks:
        lm = res.multi_hand_landmarks[0]
        pts = [(int(p.x*w), int(p.y*h)) for p in lm.landmark]
        mp_draw.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)

    # ---------- gesture logic ----------
    if pts:
        dx, dy = pts[4][0]-pts[8][0], pts[4][1]-pts[8][1]
        dist = math.hypot(dx, dy)

        if dist < pinch_thresh and not is_pinched:
            ball_x = pts[8][0]
            ball_y = pts[8][1]
            is_pinched = True
        elif dist >= pinch_thresh:
            is_pinched = False

        v1 = np.array(pts[9])  - np.array(pts[0])
        v2 = np.array(pts[17]) - np.array(pts[5])
        ang_curr  = math.degrees(math.atan2(np.cross(v1, v2), np.dot(v1, v2)))
        ang_delta = ang_curr - angle_prev
        if abs(ang_delta) < 90:
            ball_angle = (ball_angle + ang_delta) % 360
        angle_prev = ang_curr

        if dist < pinch_thresh and ((pts[8][0]-cx)**2 + (pts[8][1]-cy)**2 < radius**2):
            cx, cy = pts[8]

    # ---------- draw ball ----------
    end_x = int(cx + radius*math.cos(math.radians(ball_angle)))
    end_y = int(cy + radius*math.sin(math.radians(ball_angle)))
    cv2.circle(frame, (cx, cy), radius, (0,128,255), -1)
    cv2.line(frame, (cx, cy), (end_x, end_y), (255,255,255), 4)

    cv2.imshow("Hand-Ball Control", frame)
    if cv2.waitKey(1) & 0xFF in (27, ord('q')):   # ESC or q
        break

vid.release()
cv2.destroyAllWindows()