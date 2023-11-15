#importing Open CV module
import cv2

#Capturing the video
cap=cv2.VideoCapture(0)

while True:
    #read the caputured video
    ret,frame = cap.read()
    #To show the video
    cv2.imshow('Video', frame)

    #Break the loop if we press the key
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

#Release and destroy all windows
cap.release()
cv2.destroyAllWindows()