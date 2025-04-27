# Face Recognition System

A comprehensive face recognition system with additional features like age, gender, and emotion detection built with Python and OpenCV.

## Features

- 👤 Face Detection and Recognition
- 👥 Multiple User Management
- 🎭 Emotion Detection
- 👶👴 Age & Gender Prediction
- 🖼️ Easy-to-use GUI Interface
- 📊 Real-time Processing
- 💾 Data Collection Tool

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



