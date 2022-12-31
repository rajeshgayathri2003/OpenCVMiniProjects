import numpy as np
import cv2


x, y = 100,100
flagx = 0
flagy = 0
dx, dy = 1,1
while True:
    
    
    x = x+dx
    y = y+dy
    #print(dx, dy)
    #print(x,y)
    background = np.zeros((480, 640,3), dtype= 'uint8')
    cv2.circle(background, (x,y), 25, (0,0,255), -1)
    
    
    
    if y>=480:
        dy = -1
    if y<=0:
        dy = 1
        
    if x>=640:
        dx = -1
    if x<=0:
        dx = 1
    cv2.imshow("background", background)
    
    k = cv2.waitKey(1)
    if k == 27:
        break
    else:
        continue
    