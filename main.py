import cv2
import time

from camera.webcam import Webcam
from mediapipe_model.mp_gesture import MediaPipeHandDetector
from mapper.gesture_to_command import execute


cam = Webcam()
mp_detector = MediaPipeHandDetector()

last_executed_gesture = None
current_gesture = None
gesture_frame_count = 0

STABLE_FRAMES = 15  


while True:
    frame = cam.get_frame()
    if frame is None:
        continue

    result = mp_detector.process(frame)

    detected_gesture = "NONE"

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_detector.draw_landmarks(frame, hand_landmarks)
            detected_gesture = mp_detector.classify_gesture(hand_landmarks)

    print("Detected:", detected_gesture)

    if detected_gesture == "NONE":
        current_gesture = None
        gesture_frame_count = 0

    else:
        if detected_gesture == current_gesture:
            gesture_frame_count += 1
        else:
            current_gesture = detected_gesture
            gesture_frame_count = 1

        if (
           gesture_frame_count == STABLE_FRAMES
           and current_gesture != last_executed_gesture
           ):
           print("Executing:", current_gesture)
        try:
           execute(current_gesture)
        except Exception as e:
           print("ERROR INSIDE execute():", e)

    last_executed_gesture = current_gesture

    


    last_executed_gesture = current_gesture



    cv2.putText(
        frame,
        f"Gesture: {detected_gesture}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Gesture Controlled Drone", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()

