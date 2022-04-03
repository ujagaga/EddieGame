import pygame as pg 

import screen0,screen1,screen2,screen3,screen5
import time

pg.init()

# screen = pg.display.set_mode((1080,720))
done = False

userName = ""

screen1_disp = True
screen0_disp = False

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
x,y = screen.get_size()

screen = pg.display.set_mode((x, y))
# x,y = screen.get_size()
# print(x,y)
curScreen = 0

screen3.switchOffAll()

def resetGame():
	global screen1_disp,userName

	userName = ""
	screen1_disp = False

# screen5.prepareLeaderboard()
# screen5.ShowScreen(pg,screen)

while not done:
	if screen0_disp==False:
		screen0.ShowScreen(x,y,pg,screen)
		screen0_disp = True
		screen1_disp = False
		curScreen = 1
	# done = True
	if screen1_disp==False:
		screen1.ShowScreen(pg,screen)
		screen1_active = True
		screen1_disp = True

	if screen3.gameComplete==True:
		print("Screen 3 game complete")
		curScreen=4
		screen3.gameComplete = False

		score = screen3.score
		screen3.score = 0
		screen5.updateScores(userName,score)
		screen5.prepareLeaderboard()
	
	for event in pg.event.get():  
		if event.type == pg.QUIT:  
			done = True

		if curScreen==1:
			screen1.displayText(pg,screen,userName)
			
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_BACKSPACE:
					try:
						userName = userName[:-1]
						screen1.backspace(pg,screen,userName)
					except:
						userName = userName
				else:
					userName += event.unicode

				if event.key == pg.K_RETURN:
					curScreen = 2
					screen2.ShowScreen(pg,screen)
					curScreen =3
					screen3.generateMapping()
					screen3.ShowScreen(pg,screen)

		if curScreen==4:
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					curScreen = 5
					screen5.ShowScreen(pg,screen)
					time.sleep(1)

		elif curScreen==5:
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					print("GAME RESETTING")
					resetGame()
					curScreen = 1

	pg.display.flip()
	# pass

pg.quit()	