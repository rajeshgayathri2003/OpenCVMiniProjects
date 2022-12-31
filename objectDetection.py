import cv2
import numpy as np

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

classes = []

with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
    
print(classes)

layerNames = net.getLayerNames()

outputLayers = [layerNames[i - 1] for i in net.getUnconnectedOutLayers()]

boxes = []
confidences = []
classIDs = []
img = cv2.VideoCapture(0)
while True:
    _, frame = img.read()
    height, width, channels = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0,0,0), True, crop =  False)
    
   
            
    net.setInput(blob)
    outs = net.forward(outputLayers)
    
    for out in outs:
        for detection in out:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > 0.5:
                centerX = int(detection[0] * width)
                centerY = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(centerX - w/2)
                y = int(centerY - h/2)
                
                boxes.append([x,y,w,h])
                confidences.append(float(confidence))
                classIDs.append(classID)
                
    
            
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4 )    
    
    leng = len(boxes)
    for i in range(leng):
        if i in indexes:
            x,y,w,h = boxes[i]
            label = classes[classIDs[i]]
            label = str(label)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y+ 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2 )
            print(label)
        
    cv2.imshow("window" ,frame)
    if cv2.waitKey(1) == 27:
        break
