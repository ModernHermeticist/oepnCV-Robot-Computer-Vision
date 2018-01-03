import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)#top right
img = cv2.rectangle(img,(0,384),(128,510),(255,0,0),3)#bottom left
img = cv2.rectangle(img,(384,384),(510,510),(0,255,0),3)#bottom right
img = cv2.rectangle(img,(0,0),(128,128),(255,0,0),3)#top left

font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img, 'THIS IS A TEST', (10,500), font, 1.8, (255,255,255), 2, cv2.LINE_AA)

cv2.imwrite('randomrectangle.png', img)