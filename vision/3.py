import numpy as np
import cv2

cap = cv2.VideoCapture(1)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
    	# Our operations on the frame come here
    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    	out.write(frame)

    	# Display the resulting frame
    	cv2.imshow('frame', gray)
    	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()