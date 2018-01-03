import cv2

cameraCapture = cv2.VideoCapture(0)
fps = 30 #making this an assumption

size = (int(cameraCapture.get(cv2.CV_CAP_PROP_FRAME_WIDTH)),
		int(cameraCapture.get(cv2.CV_CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.videoWriter(
	'OutputVid.avi', cv2.cv.CV_FOURCC('P','I','M','1'), fps, size)

success, frame = cameraCapture.read()
numFramesRemaining = 10 * fps - 1

while success and numFramesRemaining > 0:
	videoWriter.write(frame)
	success, frame = cameraCapture.read()
	numFramesRemaining -= 1