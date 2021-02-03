import cv2

image = cv2.imread('tigre.jpg',0)
cv2.imshow('Tiger',image)
cv2.waitKey(0)
cv2.destroyAllWindows()