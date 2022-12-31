import cv2
import numpy as np
import dlib
from math import hypot

video = cv2.VideoCapture(0)
nose_image = cv2.imread("pigNose.jpeg")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
#nose_Area = None
while True:
    _, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,225,0), 3)
        landmarks = predictor(gray, face)
        
        top_nose = (landmarks.part(29).x, landmarks.part(29).y)
        center_nose = (landmarks.part(30).x, landmarks.part(30).y)
        left_nose = (landmarks.part(31).x, landmarks.part(31).y)
        right_nose = (landmarks.part(35).x, landmarks.part(35).y)
        
        nose_width = int(hypot((right_nose[0]-left_nose[0]),(right_nose[1]-left_nose[1])))
        nose_height = int(nose_width*0.77)
        
        
        
        noseArea = frame[left_nose[1]-nose_height: left_nose[1]-nose_height + nose_height, 
                         left_nose[0]: left_nose[0]+ nose_width]
        #cv2.rectangle(frame, (left_nose[0], left_nose[1]+2*(center_nose[1]-left_nose[1])), (right_nose[0], right_nose[1]), (255,0,0), 3)
        nose_pig = cv2.resize(nose_image, (nose_width, nose_height) )
        nose_pig_gray = cv2.cvtColor(nose_pig, cv2.COLOR_BGR2GRAY)
        _, nose_mask = cv2.threshold(nose_pig_gray, 25, 255, cv2.THRESH_BINARY_INV)
        
        nose_area_no_area = cv2.bitwise_and(noseArea, noseArea, mask= nose_mask)
        finalNose = cv2.add(nose_area_no_area, nose_pig)
        
        frame[left_nose[1]-nose_height: left_nose[1]-nose_height + nose_height, 
                         left_nose[0]: left_nose[0]+ nose_width] = nose_pig
        cv2.imshow("Nose area", noseArea) 
        cv2.imshow("Nose Mask", nose_mask)      
    cv2.imshow("Frame", frame)
    
    
    #cv2.imshow("Nose", nose_pig)
    key = cv2.waitKey(1)
    if key == 27:
        break