import cv2

face = cv2.CascadeClassifier('upn.xml')
image = cv2.imread('pastelito.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

rostros  = face.detectMultiScale(gray,scaleFactor=1.1,
                                 minNeighbors=5,
                                 minSize=(30,30),
                                 maxSize=(200,200)
                                 )
for (x,y,w,h) in rostros:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()