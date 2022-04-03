def ShowScreen(pg,screen,score):
	# show get ready
	x, y = screen.get_size()
	image = pg.image.load("media/countdown/getReady_1.jpg")
	image = pg.transform.scale(image, (x, y))

	screen.blit(image,(0,0))

	fontSize = x//10
	textObj = pg.font.Font('freesansbold.ttf',fontSize)
	text_surface = textObj.render(f"Game Over", True, (0,0,0))

	screen.blit(text_surface, (x//10,y//3))

	textObj = pg.font.Font('freesansbold.ttf',fontSize-fontSize//3)
	text_surface = textObj.render(f"Score: {score}", True, (0,0,0))

	screen.blit(text_surface, (x//4,y-y//3))

	pg.display.update()
