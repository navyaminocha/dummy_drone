import cv2
import os

gesture = input("Enter gesture name: ")
save_path = f"dataset/{gesture}"
os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)
count = len(os.listdir(save_path))
print(f"Starting from image number: {count}")



while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.putText(frame, f"Gesture: {gesture}", (20,40),
                
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Collecting Data", frame)

    key = cv2.waitKey(1)

    if key == ord('c'):
        cv2.imwrite(f"{save_path}/{count}.jpg", frame)
        count += 1
        print("Saved:", count)

    if key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
