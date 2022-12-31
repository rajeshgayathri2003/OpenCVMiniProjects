import cv2
import numpy as np
shapes = cv2.imread("IMG4.jpeg", cv2.IMREAD_GRAYSCALE)
shapes_copy = cv2.imread("IMG4.jpeg", cv2.IMREAD_COLOR)
shapes = cv2.GaussianBlur(shapes, (3,3), 0)
ret, shapes = cv2.threshold(shapes, 150, 255, cv2.THRESH_BINARY_INV + 
                                            cv2.THRESH_OTSU) 


kernel = np.ones((5, 5), np.uint8)
img_erosion = cv2.erode(shapes, kernel, iterations=3)
img_dilation = cv2.dilate(shapes, kernel, iterations=3)
contours, hierarchy  =cv2.findContours(shapes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#rint(contours)
#shapes = cv2.Sobel(src=shapes, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
cv2.drawContours(image=shapes_copy, contours= contours, contourIdx=-1, color= (0,255,0), thickness=1)

print(len(contours))

for contour in contours:
    approx = cv2.approxPolyDP(
        contour, 0.05 * cv2.arcLength(contour, True), True)
    if len(approx) == 4:
        x,y,w,h = cv2.boundingRect(contour)
        ratio = float(w)/h
        if ratio>=0.9 and ratio<1.1:
            print('Square')
            cv2.putText(img= shapes_copy,text="Square" ,org=contour[0][0], fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color= (0,0,255))
        else:
            print('Rectangle')
            cv2.putText(img= shapes_copy,text="Rectangle" ,org=contour[0][0], fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color= (0,0,255))
    else:
        print(len(approx))
            
            
cv2.imshow('image', shapes_copy)
cv2.waitKey()