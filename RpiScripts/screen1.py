input_rect = None

def ShowScreen(pg,screen):
	global input_rect

	x, y = screen.get_size()


	image = pg.image.load('media/homeScreen_1.png')
	image = pg.transform.scale(image, (x, y))

	screen.fill((0,0,0))
	screen.blit(image,(0,0))

	input_rect = pg.Rect(x//10, y//2,x-x//4,y//7)

	pg.draw.rect(screen, (0,0,0), input_rect)
	
	# TextSurf, TextRect = text_objects("Insert Your Name", largeText)
	# TextRect.center = ((x//2),(y//2))

	pg.display.flip()

def displayText(pg,screen,user_text):
	user_text = user_text.replace("\r","")
	user_text = user_text.strip()
	fontSize = 80
	textObj = pg.font.Font('freesansbold.ttf',fontSize)
	text_surface = textObj.render(user_text, True, (255,255,255))

	screen.blit(text_surface, (input_rect.x+5, input_rect.y+10))
	pg.display.flip()

def backspace(pg,screen,user_text):

	pg.draw.rect(screen, (0,0,0), input_rect)
	pg.display.flip()

	displayText(pg,screen,user_text)