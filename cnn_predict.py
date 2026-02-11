import cv2
import numpy as np
from keras.models import load_model

img_size = 128

model = load_model("gesture_cnn.keras")

class_names = ['down','flip','land','left','right','takeoff','up']

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
       continue

    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape
    crop = min(h, w) // 2

    y1 = h//2 - crop//2
    y2 = h//2 + crop//2
    x1 = w//2 - crop//2
    x2 = w//2 + crop//2

    roi = frame[y1:y2, x1:x2]

    img = cv2.resize(roi, (img_size, img_size))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img, verbose=0)

    confidence = float(np.max(pred))
    index = int(np.argmax(pred))

    gesture = class_names[index] if confidence >= 0.6 else "UNKNOWN"

    print("RAW:", np.round(pred, 3), "--", gesture)

    cv2.putText(frame, f"CNN: {gesture} ({confidence:.2f})",
            (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)




    cv2.imshow("CNN Gesture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    print(pred)


cap.release()
cv2.destroyAllWindows()

