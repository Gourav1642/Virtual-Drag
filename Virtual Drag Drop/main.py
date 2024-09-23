import cv2
import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector

from cvzone.HandTrackingModule import HandDetector

# Initialize video capture and hand detector
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(maxHands=1)
colorR=(255,0,255)

cx,cy,w,h=100,100,200,200


while True:
    # Capture image from the camera
    success, img = cap.read()
    img=cv2.flip(img,1)

    # Detect hands in the image
    hands, img = detector.findHands(img,draw=False)  # Detect hands

    if hands:
        # Get the landmarks of the first hand
        hand = hands[0]
        lmList = hand["lmList"]  # List of 21 landmark points
        
        cursor = lmList[8]  # Landmark 8 corresponds to the tip of the index finger
        if cx-w //2<cursor[0]<cx+w //2 and cy-h //2<cursor[1]<cy+h //2:
            colorR=0,255,0
            cx,cy=cursor[0],cursor[1]
        else:
            colorR=(255,0,255)
    
    cv2.rectangle(img,(cx-w //2,cy-h //2),(cx+w //2,cy+h //2),colorR,cv2.FILLED)
    # Display the image
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
