import cv2
import face_recognition
import os

# Dictionary to store names and corresponding encodings
people_encodings = {}

# Function to load image and create encoding
def load_encoding(name, path):
    image = face_recognition.load_image_file(path)
    encoding = face_recognition.face_encodings(image)[0]
    return name, encoding

# Add people and their encodings
people_encodings['Amal'] = load_encoding('Amal', '/Users/Amal/Desktop/amal.jpg')
people_encodings['Midhun'] = load_encoding('Midhun', '/Users/Amal/Desktop/Midhun.png')

# Get a reference to the webcam
video_capture = cv2.VideoCapture(0)

# Set lower resolution for video capture
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # Capture each frame from the webcam
    ret, frame = video_capture.read()

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check for matches with each person
        for name, encoding in people_encodings.values():
            matches = face_recognition.compare_faces([encoding], face_encoding)
            if True in matches:
                # Draw a rectangle around the face and display the name
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()