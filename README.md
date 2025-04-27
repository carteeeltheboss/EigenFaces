# Face Recognition System

A comprehensive face recognition system with additional features like age, gender, and emotion detection built with Python and OpenCV.

## Features

-  Face Detection and Recognition
-  Multiple User Management
-  Emotion Detection
-  Age & Gender Prediction
-  Easy-to-use GUI Interface
-  Real-time Processing
-  Data Collection Tool

## Prerequisites

- Python 3.7.12
- Webcam or integrated camera
- Windows/Linux/Mac OS

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/FaceRecognition-GUI-APP.git
cd FaceRecognition-GUI-APP
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages
```bash
pip install -r req.txt
```

## Usage

1. Run the application
```bash
python app-gui.py
```

2. Main Functions:
   - **Detect Faces**: Start face recognition for registered users
   - **Add New User**: Register a new user by capturing face data
   - **Age & Gender Detection**: Detect age and gender of faces
   - **Emotion Detection**: Analyze facial emotions
   
3. Adding a New User:
   - Click "Add New User"
   - Enter username
   - The system will capture 300 images of your face
   - Wait for training completion

4. Recognition:
   - Click "Detect Faces"
   - The system will recognize registered users
   - Press 'q' to quit the recognition window

## Dependencies

### Core Machine Learning
- TensorFlow (2.7.0)
- Keras (2.7.0)
- NumPy (1.19.5)
- scikit-learn (latest)

### Computer Vision
- OpenCV (4.2.0.34)
  - opencv-python
  - opencv-contrib-python
- Pillow (9.0.1)
- imutils (0.5.3)
- MTCNN (0.1.1)

### Deep Learning Utilities
- tensorboard (2.11.2)
- tensorflow-estimator (2.7.0)
- Keras-Preprocessing (1.1.2)
- h5py (2.10.0)

### Google Services & Auth
- google-auth (2.39.0)
- google-auth-oauthlib (0.4.6)
- google-pasta (0.2.0)

### HTTP & Network
- requests (2.31.0)
- urllib3 (2.0.7)
- grpcio (1.62.3)

### Data Processing
- protobuf (3.20.3)
- flatbuffers (2.0.7)
- opt-einsum (3.3.0)

### Utilities
- six (1.17.0)
- wrapt (1.16.0)
- typing_extensions (4.7.1)
- termcolor (2.3.0)
- Werkzeug (2.2.3)
- zipp (3.15.0)

### Authentication & Security
- rsa (4.9.1)
- oauthlib (3.2.2)
- pyasn1 (0.5.1)
- pyasn1-modules (0.3.0)

### Text Processing
- Markdown (3.4.4)
- MarkupSafe (2.1.5)

### Miscellaneous
- absl-py (2.1.0)
- astunparse (1.6.3)
- cachetools (5.5.2)
- certifi (2025.4.26)
- charset-normalizer (3.4.1)
- gast (0.4.0)
- idna (3.10)
- importlib-metadata (6.7.0)
- libclang (18.1.1)

## Quick Installation

Install all dependencies using:
```bash
pip install -r requirements.txt
```

For GPU support (recommended for better performance):
```bash
pip install tensorflow-gpu==2.7.0
```

Note: Some packages may require additional system-level dependencies. Please refer to their respective documentation for complete installation guides.



