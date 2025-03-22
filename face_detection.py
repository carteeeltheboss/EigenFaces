import cv2
import os

# Configurer le nom de la personne
person_name = "fatine"
os.makedirs(f"dataset/{person_name}", exist_ok=True)

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
count = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face_roi = gray[y:y+h, x:x+w]
        cv2.imwrite(f"dataset/{person_name}/face_{count}.jpg", face_roi)
        count += 1
    
    cv2.imshow('Capture Faces', frame)
    if cv2.waitKey(1) == ord('q') or count >= 50:  # Capture 50 images
        break

cap.release()
cv2.destroyAllWindows()