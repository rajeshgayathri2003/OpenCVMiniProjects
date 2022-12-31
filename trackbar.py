import cv2

final = cv2.imread("final.jpg")

def nothing(x):
    pass

dimensions = final.shape
print(dimensions)
cv2.namedWindow("image")
cv2.createTrackbar("xAxis", "image", 0, 266, nothing )
val = None
while True:
    cv2.imshow("image", final)
    k = cv2.waitKey()
    if k == 27:
        break
    val = cv2.getTrackbarPos("xAxis", "image")


print(val)
