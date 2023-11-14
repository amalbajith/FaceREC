# FaceREC
 The provided Python code leverages facial recognition technology to identify individuals in real-time using a webcam. Developed with the face_recognition library, the program captures video frames, detects faces, and compares them with preloaded facial encodings of known individuals stored in a dictionary.


# Facial Recognition System

## Introduction

This project utilizes facial recognition technology to identify individuals in real-time using a webcam. The program captures video frames, detects faces, and compares them with preloaded facial encodings of known individuals.

## Installation

### Prerequisites

- Python installed on your machine.
- [pip](https://pip.pypa.io/en/stable/installation/) for package installation.

### Clone the Repository

```bash
git clone https://github.com/your-username/FacialRecognitionAttendance.git
cd FacialRecognitionAttendance


Install Dependencies

pip install face_recognition opencv-python

Update File Paths:
Open the script (your_script_name.py) and update the file paths for images in the people_encodings dictionary. Replace the placeholder paths with the actual paths to your image files.

Usage
Run the Script:

python your_script_name.py

Notes
Ensure your webcam is connected and accessible.
Adjust the webcam resolution in the script if needed (cv2.CAP_PROP_FRAME_WIDTH and cv2.CAP_PROP_FRAME_HEIGHT).
Customize the code for your specific use case by adding more people to the people_encodings dictionary.

