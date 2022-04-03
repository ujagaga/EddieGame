from pygame import mixer
import time

mixer.init()
mixer.music.load("media/beep02.wav")
mixer.music.set_volume(0.7)

def ShowScreen(pg,screen):
	# show get ready
	x, y = screen.get_size()
	image = pg.image.load("media/countdown/getReady.png")
	image = pg.transform.scale(image, (x, y))

	screen.blit(image,(0,0))
	pg.display.update()

	pg.time.wait(1000)
	
	for i in range(10):

		image = pg.image.load(f"media/countdown/getReady_{10-i}.jpg")
		image = pg.transform.scale(image, (x, y))

		screen.blit(image,(0,0))

		fontSize = x//5
		textObj = pg.font.Font('freesansbold.ttf',fontSize)
		text_surface = textObj.render(f"{10-i}", True, (0,0,0))

		screen.blit(text_surface, (x//2,y//2))
		mixer.music.play()

		pg.display.update()

		time.sleep(0.1)