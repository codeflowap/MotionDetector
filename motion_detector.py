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
    # Assigns 255 color to pixles in delta_frame where diff is more than 20 in intensity
    thresh_frame = cv2.threshold(delta_frame, 20, 255, cv2.THRESH_BINARY)[1]
    # Smooth threshold frame
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Find all counters. (_,cnts) = contours, hierarchy
    # This should be resolved
    (_,cnts) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if cnts is None:
        continue
    else:
        for contour in cnts:
            print("contour is", contour)
            #(x,y,w,h) = cv2.boundingRect(contour)
            #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
     
    cv2.imshow("Captured",gray)
    cv2.imshow("Difference",delta_frame)
    cv2.imshow("Trshold",thresh_frame)
    cv2.imshow("Final",frame)
    
    key = cv2.waitKey(1000)
    #print(gray)
    
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows
