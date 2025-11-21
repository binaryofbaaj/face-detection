import cv2

haarcascade = "/Users/gurmansingh/Desktop/face-detection/models/haarcascade_frontalface_default.xml"
 
cap=cv2.VideoCapture(0)

cap.set(3,640) #width
cap.set(4,480) #height 

while True:
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    face_cascade=cv2.CascadeClassifier(haarcascade)
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('Face Detection',frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cv2.imshow("face Detection",frame)

if cv2.waitKey(0) & 0xFF==ord('q'):
    cv2.destroyAllWindows()
    cap.release()