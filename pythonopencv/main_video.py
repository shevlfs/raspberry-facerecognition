import cv2
from simple_facerec import SimpleFacerec
import cmake

import numpy as np
# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255,255,255), 2)
    # img = cv2.imread("images/dima utkin.jpg")
    # Hori = np.concatenate((frame, img), axis=1)
    # cv2.imshow('HORIZONTAL', Hori)
    cv2.imshow("Frame", frame)


    key = cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()