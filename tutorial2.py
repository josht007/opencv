import cv2
import random

img = cv2.imread('assets/dunl.jfif', 1) 

tag = img[100:180, 50:70]
img[2:82, 100:120] = tag

# for i in range(100):
#     for j in range(img.shape[0]):
#         img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0, 255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()