import cv2
import numpy as np
import joblib

# Charger les modèles
pca = joblib.load("pca_model.pkl")
model = joblib.load("svm_model.pkl")

# Charger les labels avec allow_pickle=True
data = np.load("preprocessed_data.npz", allow_pickle=True)
label_dict = data["labels"].item()

# Initialiser la webcam
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        resized = cv2.resize(face_roi, (64, 64))
        normalized = resized.flatten() / 255.0
        projected = pca.transform([normalized])
        pred = model.predict(projected)
        proba = model.predict_proba(projected)[0].max()
        
        if proba > 0.8:
            label = label_dict[pred[0]]
        else:
            label = "Inconnu"
        
        cv2.putText(frame, f"{label} ({proba*100:.1f}%)", (x, y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow('Reconnaissance Faciale', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()