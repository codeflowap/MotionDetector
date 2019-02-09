import cv2, time

first_frame = None


video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if first_frame is None
        first_frame = gray
        continue
    
    cv2.imshow("Captured",gray)
    
    key = cv2.waitKey(1)
    print(gray)
    
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows
