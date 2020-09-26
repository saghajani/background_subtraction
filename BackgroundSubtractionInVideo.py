import numpy as np
import cv2

# Capture a video by webcam
cap = cv2.VideoCapture(0)
# Or Capture from a saved file
# cap = cv2.VideoCapture('input.mp4')
# Create BackgroundSubtractor object
fgbg = cv2.createBackgroundSubtractorMOG2()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MP42') #DIVX XVID
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        fgmask = fgbg.apply(frame)

        out.write(fgmask)

        cv2.imshow('Original',frame)
        cv2.imshow('Background Removed',fgmask)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()