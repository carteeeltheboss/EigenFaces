import cv2
import numpy as np
import os

def preprocess_dataset(input_dir="dataset", output_size=(64, 64)):
    faces = []
    labels = []
    label_dict = {}
    current_label = 0
    
    for person_name in os.listdir(input_dir):
        person_dir = os.path.join(input_dir, person_name)
        if not os.path.isdir(person_dir):  # Skip if not a directory
            continue
        label_dict[current_label] = person_name
        
        for img_name in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, output_size)
            img = img / 255.0  # Normalisation
            faces.append(img.flatten())
            labels.append(current_label)
        
        current_label += 1
    
    return np.array(faces), np.array(labels), label_dict

# Exécuter le prétraitement
X, y, label_dict = preprocess_dataset()
np.savez_compressed("preprocessed_data.npz", X=X, y=y, labels=np.array([label_dict], dtype=object))

#np.savez("preprocessed_data.npz", X=X, y=y, labels=label_dict)