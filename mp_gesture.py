import cv2
import mediapipe as mp
import math

class MediaPipeHandDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7)
        self.mp_draw = mp.solutions.drawing_utils

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(rgb)

    def draw_landmarks(self, frame, hand_landmarks):
        self.mp_draw.draw_landmarks(
            frame,
            hand_landmarks,
            self.mp_hands.HAND_CONNECTIONS
        )
    

    def distance(self, p1, p2):
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

    def classify_gesture(self, hand_landmarks):
      lm = hand_landmarks.landmark

    # 🔥 SAFETY CHECK (THIS FIXES THE CRASH)
      if lm is None or len(lm) < 21:
        return "NONE"
      
      thumb_tip = lm[4]
      index_tip = lm[8]
      index_pip = lm[6]

      middle_tip = lm[12]
      middle_pip = lm[10]

      ring_tip = lm[16]
      ring_pip = lm[14]

      pinky_tip = lm[20]
      pinky_pip = lm[18]

      
      wrist = lm[0]
      index_mcp = lm[5]

    # ---------- TAKEOFF (open palm) ----------
      if (
        index_tip.y < index_pip.y and
        middle_tip.y < middle_pip.y and
        ring_tip.y < ring_pip.y and
        pinky_tip.y < pinky_pip.y
       ):
        return "TAKEOFF"

    # ---------- LAND (fist) ----------
      if (
        index_tip.y > index_pip.y and
        middle_tip.y > middle_pip.y and
        ring_tip.y > ring_pip.y and
        pinky_tip.y > pinky_pip.y
        ):
        return "LAND"
    
    # ----------- FLIP (OK gesture) -----------
      if (
        self.distance(thumb_tip, index_tip) < 0.05 and
        middle_tip.y < middle_pip.y and
        ring_tip.y < ring_pip.y and
        pinky_tip.y < pinky_pip.y
         ):
        return "FLIP"

    # ---------- UP ----------
      if index_tip.y < index_pip.y:
        return "UP"

    # ---------- DOWN ----------
      if index_tip.y > index_pip.y + 0.05:
        return "DOWN"

    # ---------- LEFT ----------
      if wrist.x > index_mcp.x + 0.05:
        return "LEFT"

    # ---------- RIGHT ----------
      if wrist.x < index_mcp.x - 0.05:
        return "RIGHT"

      return "NONE"

