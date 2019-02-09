import cv2, time

background = None


video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0) 

    if background is None:
        background = gray
        continue

    delta_frame = cv2.absdiff(background,gray)

    
    cv2.imshow("Captured",gray)
    cv2.imshow("Difference",delta_frame)
    
    key = cv2.waitKey(1)
    print(gray)
    
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows
