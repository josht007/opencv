import cv2

img = cv2.imread('assets/dunl.jfif', 1) 
img = cv2.resize(img, (0, 0), fx=2, fy=2)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.sjpeg', img)

cv2.imshow('Dunked on', img)

cv2.waitKey(0)

cv2.destroyAllWindows()