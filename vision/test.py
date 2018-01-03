from filters import *
import cv2
import numpy

#randomBtyeArray = numpy.random.randint(0,256,120000)

#dst = numpy.array(randomBtyeArray)
#src = numpy.array(randomBtyeArray)

src = cv2.imread('src.png')
dst = cv2.imread('src.png')

strokeEdges(src, dst)

cv2.imwrite('dst.png', dst)