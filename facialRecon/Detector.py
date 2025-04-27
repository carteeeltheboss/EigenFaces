import cv2
from time import time
import os
from PIL import Image
from tkinter import messagebox

def main_app(timeout=10):
    face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
    recognizers = {}
    detected_people = set()  # Store unique detections
    
    # Load all classifiers
    classifier_path = "./data/classifiers/"
    for classifier_file in os.listdir(classifier_path):
        if classifier_file.endswith("_classifier.xml"):
            user_name = classifier_file.replace("_classifier.xml", "")
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read(os.path.join(classifier_path, classifier_file))
            recognizers[user_name] = recognizer

    cap = cv2.VideoCapture(0)
    start_time = time()
    
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Add instruction text at the bottom of the frame
        cv2.putText(frame, "Press 'q' to quit", (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            max_confidence = 0
            recognized_name = None

            for user_name, recognizer in recognizers.items():
                id, confidence = recognizer.predict(roi_gray)
                confidence = 100 - int(confidence)
                
                if confidence > max_confidence and confidence > 50:
                    max_confidence = confidence
                    recognized_name = user_name
            
            if recognized_name:
                detected_people.add((recognized_name, max_confidence))  # Add to set
                text = f'Recognized: {recognized_name.upper()} ({max_confidence}%)'
                color = (0, 255, 0)
            else:
                text = "Unknown Face"
                color = (0, 0, 255)
                
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        cv2.imshow("Face Recognition - Press 'q' to quit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    # Convert set to list and sort by confidence
    results = sorted(list(detected_people), key=lambda x: x[1], reverse=True)
    
    # Show results in message box
    if results:
        result_text = "Recognized People:\n\n"
        for name, conf in results:
            result_text += f"{name}: {conf}% confidence\n"
        messagebox.showinfo("Recognition Results", result_text)
    
    return results


