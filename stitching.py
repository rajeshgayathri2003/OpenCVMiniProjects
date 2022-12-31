import cv2
"""
def clickEvent(event, image, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'({x},{y})')
        cv2.putText(image, f'({x}, {y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.circle(image, (x,y), 3, (0,255,255), -1)
        
cv2.namedWindow("Image")
image = cv2.imread("final.jpg")
cv2.setMouseCallback("Image", clickEvent)

while True:
    cv2.imshow("Image", image)
    k = cv2.waitKey(1)
    if k == 27:
        break
    
cv2.destroyAllWindows()
    
"""
    
import cv2

# define a function to display the coordinates of

# of the points clicked on the image
'''def clickEvent(event, x, y, flags, params):
   if event == cv2.EVENT_LBUTTONDOWN:
      print(f'({x},{y})')
      
      # put coordinates as text on the image
      cv2.putText(img, f'({x},{y})',(x,y),
      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
      
      # draw point on the image
      cv2.circle(img, (x,y), 3, (0,255,255), -1)
''' 
# read the input image
img = cv2.imread('final.jpg')
print(img.shape)
'''
# create a window
cv2.namedWindow('Point Coordinates')

# bind the callback function to window
cv2.setMouseCallback('Point Coordinates', clickEvent)

# display the image
while True:
   cv2.imshow('Point Coordinates',img)
   k = cv2.waitKey(1) 
   if k == 27:
      break
cv2.destroyAllWindows()
'''
new_1 = img[0:120, 0:140]
new_2 = img[0:70, 140:266]
new_3 = img[120:188, 0:140]
new_4 = img[70: 188, 140:266]
#cv2.imshow("window", new_1)
#cv2.imshow("window2", new_2)
#cv2.imshow("window3", new_3)
#cv2.imshow("window4", new_4)

img_lst = [new_1, new_2, new_3, new_4]
img_lst = [cv2.resize(x, (0,0), fx=0.4, fy =0.4 ) for x in img_lst]
stitchy = cv2.Stitcher.create()
(dummy, output) = stitchy.stitch(img_lst)

if dummy != cv2.STITCHER_OK:
    print("Unsuccessful")
else:
    print("Worked")
    
print(output)
#cv2.imshow("OUTPUT", output)
#cv2.waitKey()