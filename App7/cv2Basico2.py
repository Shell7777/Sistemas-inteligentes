import cv2

image = cv2.imread('tigre.jpg',1)
image_amp = cv2.resize(image,(200,200))

cv2.imshow('Tiger',image)
cv2.waitKey(0)
cv2.destroyAllWindows()