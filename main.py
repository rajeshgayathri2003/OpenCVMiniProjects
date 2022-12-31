
import cv2
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

date_ = date.today().strftime("%d/%m/%Y")

canvas = np.ones((600, 600, 3))
cv2.rectangle(canvas, 
              pt1=(50,50),
              pt2=(100,150),
              color=(255,0,0),
              thickness=5
              )

cv2.putText(img= canvas,text="Hello" ,org=(50,200), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 1, color= (0,0,255))
cv2.putText(img= canvas,text=date_ ,org=(50,250), fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 1, color= (0,0,255))

plt.imshow(canvas)



shapes = cv2.imread("IMG4.jpeg", cv2.IMREAD_GRAYSCALE)
shapes_copy = cv2.imread("IMG4.jpeg", cv2.IMREAD_COLOR)
shapes = cv2.GaussianBlur(shapes, (5,5), 0)
ret, shapes = cv2.threshold(shapes, 150, 255, cv2.THRESH_BINARY_INV + 
                                            cv2.THRESH_OTSU) 
kernel = np.ones((5, 5), np.uint8)
img_erosion = cv2.erode(shapes, kernel, iterations=1)
img_dilation = cv2.dilate(shapes, kernel, iterations=1)


contours, hierarchy  =cv2.findContours(shapes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#rint(contours)
#shapes = cv2.Sobel(src=shapes, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
cv2.drawContours(image=shapes_copy, contours= contours, contourIdx=-1, color= (0,255,0), thickness=3)

for contour in contours:
    print(type(contour))
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)
    if len(approx) == 3:
        print('Triangle')
        
        cv2.putText(img= shapes_copy,text="Triangle" ,org=contour[0][0], fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color= (0,0,255))
        
    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(contour)
        ratio = float(w)/h
        if ratio>=0.9 and ratio<1.1:
            print('Square')
            cv2.putText(img= shapes_copy,text="Square" ,org=contour[0][0], fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color= (0,0,255))
        else:
            print('Rectangle')
            cv2.putText(img= shapes_copy,text="Rectangle" ,org=contour[0][0], fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color= (0,0,255))
    elif len(approx) == 5:
        print('pentagon')
        cv2.putText(img= shapes_copy,text="Pentagon" ,org=contour[0][0], fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color= (0,0,255))
    elif len(approx) == 6:
        print('Hexagon')
        cv2.putText(img= shapes_copy,text="Hexagon" ,org=contour[0][0], fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color= (0,0,255))
    else:
        print('Circle')
        cv2.putText(img= shapes_copy,text="Circle" ,org=contour[0][0], fontFace= cv2.FONT_HERSHEY_COMPLEX, fontScale= 0.5, color= (0,0,255))
        #print(contour)        
    
#cnt = contours[4]
#cv2.drawContours(shapes_copy, contours, 0, (255,0,0), 3)
cv2.imshow('image', shapes_copy)
cv2.waitKey()
#plt.imshow(shapes, cmap= 'inferno')

#cv2.imshow('image', shapes)
#cv2.waitKey()