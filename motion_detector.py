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

    # Assigns 255 color to pixles in delta_frame where diff is more than 30 intensity
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    # Smooth threshold frame
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    
    cv2.imshow("Captured",gray)
    cv2.imshow("Difference",delta_frame)
    cv2.imshow("Trshold",thresh_frame)

    key = cv2.waitKey(1)
    print(gray)
    
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows
