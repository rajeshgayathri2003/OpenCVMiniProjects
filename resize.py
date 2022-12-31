#%%
import cv2
import matplotlib.pyplot as plt
image = cv2.imread("final.jpg")
image1 = cv2.resize(image, (0,0), fx =0.5, fy = 0.5)
#plt.imshow(image, cmap= 'gray')
plt.imshow(image1, cmap= 'gray')

# %%
