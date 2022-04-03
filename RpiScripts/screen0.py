import cv2
import numpy
import os
from ffpyplayer.player import MediaPlayer

def ShowScreen(x,y,pg,screen):
	videoPath = "media/mainVideo.mov"
	os.system("omxplayer "+videoPath)
	# try:
	# 	videoPath = "media/mainVideo.mov"
	# 	vid = cv2.VideoCapture(videoPath)
	# 	player = MediaPlayer(videoPath)

	# 	fps = vid.get(cv2.CAP_PROP_FPS)
	# 	waitMs = int(numpy.round((1/fps)*1000))

	# 	while True:
	# 		try:
	# 			ret, frame = vid.read()
	# 			audio_frame, val = player.get_frame()
				
	# 			screen.fill([0, 0, 0])
				
	# 			frame = cv2.resize(frame,(x,y))

	# 			# cv2.namedWindow("test", cv2.WINDOW_FREERATIO)
	# 			# cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	# 			cv2.imshow("frame",frame)

	# 			if val != 'eof' and audio_frame is not None:
	# 				#audio
	# 				img, t = audio_frame

	# 			cv2.waitKey(1)

	# 		except Exception as e:
	# 			print("Some Error",e)	
	# 			break

	# 	vid.release()
	# 	cv2.destroyAllWindows()		

	# except Exception as e:
	# 	print("ERROR",e)
	# 	vid.release()
	# 	cv2.destroyAllWindows()		\0
