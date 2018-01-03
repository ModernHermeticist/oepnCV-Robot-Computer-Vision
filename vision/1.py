import cv2
import numpy
import os

randomBtyeArray = numpy.random.randint(0,256,120000)
flatNumpyArray = numpy.array(randomBtyeArray)

grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('RandomGray.png', grayImage)
 
bgrImage = flatNumpyArray.reshape(100,400,3)
cv2.imwrite('RandomColor.png', bgrImage)