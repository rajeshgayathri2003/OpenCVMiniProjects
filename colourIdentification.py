import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    blueCount = 0
    redCount = 0
    greenCount = 0
    yellowCount = 0
    _, frame = cap.read()
    Xcoord, Ycoord, channels = frame.shape
    #frame = cv2.imread("shapes.jpg")
    # _ returns a true value if the frame is successfully read
    intoHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Setting the lower and upper limits for blue color
    lLimitB = np.array([98,50,50], np.uint8)
    uLimitB = np.array([139,255,255], np.uint8)
    
    lLimitR = np.array([136, 87, 111], np.uint8)
    ulimitR = np.array([180, 255, 255], np.uint8)
    
    lLimitG = np.array([25, 52, 72], np.uint8)
    uLimitG = np.array([102, 255, 255], np.uint8)
    
    lLimitY = np.array([20, 80, 80], np.uint8)
    uLimitY = np.array([30, 255, 255], np.uint8)
    
    #creating the mask => only items in the range will be white => the rest black
    kernel = np.ones((5,5), "uint8")
    
    bmask = cv2.inRange(intoHSV, lLimitB, uLimitB)
    rmask = cv2.inRange(intoHSV, lLimitR, ulimitR)
    gmask = cv2.inRange(intoHSV, lLimitG, uLimitG)
    ymask = cv2.inRange(intoHSV, lLimitY, uLimitY)
    
    #bmask = cv2.dilate(bmask, kernel)
    
    blue = cv2.bitwise_and(frame, frame, mask = bmask)
    red = cv2.bitwise_and(frame, frame, mask = rmask)
    green = cv2.bitwise_and(frame, frame, mask = gmask)
    yellow = cv2.bitwise_and(frame, frame, mask = ymask)
    
    contoursB, _ = cv2.findContours(bmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contoursR, _ = cv2.findContours(rmask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contoursG, _ = cv2.findContours(gmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contoursY, _ = cv2.findContours(ymask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    for b in contoursB:
        area = cv2.contourArea(b)
        if area>300:
            x ,y ,w ,h = cv2.boundingRect(b)
            blueCount+=1
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
            cv2.putText(frame, "blue", (x,y), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 0, 0))
            cv2.putText(frame, str(blueCount), (Xcoord - 30, 30), cv2.FONT_HERSHEY_PLAIN, 2.0, (255, 0, 0))
        
    for r in contoursR:
        area = cv2.contourArea(r)
        if area>300:
            x ,y ,w ,h = cv2.boundingRect(r)
            redCount+=1
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
            cv2.putText(frame, "red", (x,y), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 255))
            cv2.putText(frame, str(redCount), (Xcoord - 30, 60), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255))
        
    for g in contoursG:
        area = cv2.contourArea(g)
        if area>300:
            x ,y ,w ,h = cv2.boundingRect(g)
            greenCount+=1
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, "green", (x,y), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 0))
            cv2.putText(frame, str(greenCount), (Xcoord - 30, 150), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 255, 0))
            
    for Y in contoursY:
        area = cv2.contourArea(Y)
        if area>300:
            x ,y ,w ,h = cv2.boundingRect(Y)
            yellowCount+=1
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)
            cv2.putText(frame, "yellow", (x,y), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,255,255))
            cv2.putText(frame, str(greenCount), (Xcoord - 30, 120), cv2.FONT_HERSHEY_PLAIN, 2.0, (0,255,255))
        
    
    cv2.imshow("Original", frame)
    #cv2.imshow("Blue", blue)
    
    if cv2.waitKey(1) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
    
    
    
    