import random
import RPi.GPIO as GPIO
import time
import screen4
from pygame import mixer
from threading import Thread

GPIO.setmode(GPIO.BCM)

mixer.init()
mixer.music.load("media/beep02.wav")
mixer.music.set_volume(0.7)
# LEDS
led1 = 2
led2 = 3
led3 = 4
led4 = 14
led5 = 1
led6 = 17
led7 = 18
led8 = 27
led9 = 22
led10 = 23
led11 = 24

#PUSH BUTTONS
btn1 = 8
btn2 = 25
btn3 = 0
btn4 = 7
btn5 = 5
btn6 = 6
btn7 = 12
btn8 = 13
btn9 = 19
btn10 = 21
btn11 = 26

allLeds = [led1,led2,led3,led4,led5,led6,led7,led8,led9,led10,led11]
allPushBtns = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11]


score = 0
gameComplete = False

for i in range(len(allLeds)):
	GPIO.setup(allLeds[i],GPIO.OUT)
	GPIO.setup(allPushBtns[i],GPIO.IN,pull_up_down=GPIO.PUD_UP)

def drawRoundedRect(pg, screen, rect, colour=(128,128,128), radius=7 ):
    x, y   = rect.topleft
    width  = rect.width
    height = rect.height
    pg.draw.circle( screen, colour, ( x+radius, y+radius ), radius )                  # TL corner
    pg.draw.circle( screen, colour, ( x+width-radius-1, y+radius ), radius )          # TR corner
    pg.draw.circle( screen, colour, ( x+radius, y+height-radius-1 ), radius )         # BL corner
    pg.draw.circle( screen, colour, ( x+width-radius-1, y+height-radius-1 ), radius ) # BR corner
    # In-fill
    pg.draw.rect( screen, colour, ( x+radius, y, width-(2*radius), height ) )
    pg.draw.rect( screen, colour, ( x, y+radius, width, height-(2*radius) ) )

def playSound():
	mixer.music.play()

def ShowScreen(pg,screen):
	global score,gameComplete
	switchOffAll()
	x, y = screen.get_size()

	image = pg.image.load("media/duringgame.png")
	image = pg.transform.scale(image, (x, y))

	screen.blit(image,(0,0))
	
	rect = pg.Rect((x//2)-(x//8),0,x//4,y//3.2)
	# pg.draw.rect(screen, (0,0,0), rect)

	drawRoundedRect(pg,screen,rect,colour=(0,0,0),radius=x//32)
	

	pg.draw.circle(screen, (0,255,0), (x//2,y//7), x//16)

	pg.display.update()

	startTime = round(time.time())
	startTimeGlobal = round(time.time())
	running = True

	delayMs = 2200

	curTime = round(time.time())
	# randomLed = random.choice(allLeds)
	randomLed = random.choice(allLeds)
	curLedIndex = allLeds.index(randomLed)
	correctPushBtn = allPushBtns[curLedIndex]
	print("Correct Push Btn",correctPushBtn)
	GPIO.output(randomLed,GPIO.HIGH)
	
	nextLed = False
	btnPressed = False

	gameWon = None

	tempBtnPressed = correctPushBtn
	fontSize = x//14

	while running:
		
		timeNow = round(time.time())
		secPassed = timeNow - startTimeGlobal
		fontSizeTime = x//42

		rect2 = pg.Rect((x//2)-(x//10),(y//3.2)-(y//17),x//5,fontSizeTime)
		pg.draw.rect(screen, (0,0,0), rect2)

		textObj = pg.font.Font('freesansbold.ttf',fontSizeTime)
		text_surface1 = textObj.render(str(60-secPassed)+" SEC", True, (255,255,255))

		screen.blit(text_surface1, ((x//2)-(x//25), (y//3.2)-(y//17)))

		rect3 = pg.Rect((x//2)-(x//8),(y//2)-(y//8),x//4,x//12)
		# pg.draw.rect(screen, (255,255,255), rect3)
		drawRoundedRect(pg,screen,rect3,colour=(255,255,255),radius=x//64)

		textObj3 = pg.font.Font('freesansbold.ttf',fontSize)
		text_surface3 = textObj3.render(str(score), True, (0,0,0))

		screen.blit(text_surface3, ((x//2)-(x//24), (y//2)-fontSize))
		
		pg.display.flip()

		if round(time.time()) - startTimeGlobal >= 60:
			running=False
			gameWon = True
			break
		if round(time.time()) - startTime > 10:
			if delayMs-100 <= 0:
				delayMs = 100
			else:
				delayMs -= 400
			startTime = round(time.time())
		# print(-(round(curTime)*1000 ) - (round(time.time())*1000))

		if ((round(time.time())*1000)-(curTime*1000) ) > delayMs or nextLed==True:
			switchOffAll()

			curTime = round(time.time())
			randomLed = random.choice(allLeds)
			curLedIndex = allLeds.index(randomLed)
			correctPushBtn = allPushBtns[curLedIndex]
			nextLed = False
			print(correctPushBtn,"Delay ms",delayMs)

			GPIO.output(randomLed,GPIO.HIGH)

			continue


		temp = allPushBtns[:]
		print("temp size:", temp)
		temp.remove(correctPushBtn)
		
		wrongBtn1 = temp[0]
		wrongBtn2 = temp[1]
		wrongBtn3 = temp[2]
		wrongBtn4 = temp[3]
		wrongBtn5 = temp[4]
		wrongBtn6 = temp[5]
		wrongBtn7 = temp[6]
		wrongBtn8 = temp[7]
		wrongBtn9 = temp[8]
		wrongBtn10 = temp[9]

		correctButtonPress = GPIO.input(correctPushBtn)

		wrongButtonPress1 = GPIO.input(wrongBtn1)
		wrongButtonPress2 = GPIO.input(wrongBtn2)
		wrongButtonPress3 = GPIO.input(wrongBtn3)
		wrongButtonPress4 = GPIO.input(wrongBtn4)
		wrongButtonPress5 = GPIO.input(wrongBtn5)
		wrongButtonPress6 = GPIO.input(wrongBtn6)
		wrongButtonPress7 = GPIO.input(wrongBtn7)
		wrongButtonPress8 = GPIO.input(wrongBtn8)
		wrongButtonPress9 = GPIO.input(wrongBtn9)
		wrongButtonPress10 = GPIO.input(wrongBtn10)


		# print(correctButtonPress,wrongButtonPress1)
		if correctButtonPress==False and btnPressed==False:
			score+=1
			btnPressed=True
			nextLed = True
			tempBtnPressed = correctPushBtn
			
			# rect = pg.Rect((x//2)-(x//8),y//2,x//4,x//12)
			# pg.draw.rect(screen, (255,255,255), rect)
			# image = pg.image.load("media/duringgame.jpg")
			# image = pg.transform.scale(image, (x, y))

			# screen.blit(image,(0,0))


			# textObj = pg.font.Font('freesansbold.ttf',fontSize)
			# text_surface = textObj.render(f"{score}", True, (0,0,0))

			# screen.blit(text_surface, (x//2,y//2))
			# pg.display.update()
			
			Thread(target=playSound,daemon=True).start()
			continue

		elif GPIO.input(tempBtnPressed)==True and btnPressed==True:
			btnPressed = False
		

		elif wrongButtonPress1==False and btnPressed==False:
			print("Wrong button pressed")
			running = False
			gameWon = False
			Thread(target=playSound,daemon=True).start()
			break		

		elif wrongButtonPress2==False and btnPressed==False:
			print("Wrong button pressed")
			running = False
			gameWon = False
			Thread(target=playSound,daemon=True).start()
			break		

		elif wrongButtonPress3==False and btnPressed==False:
			print("Wrong button pressed")
			running = False
			gameWon = False
			Thread(target=playSound,daemon=True).start()
			break		

		elif wrongButtonPress4==False and btnPressed==False:
			print("Wrong button pressed")
			running = False
			gameWon = False
			Thread(target=playSound,daemon=True).start()
			break		

		elif wrongButtonPress5==False and btnPressed==False:
			print("Wrong button pressed")
			running = False
			gameWon = False
			Thread(target=playSound,daemon=True).start()
			break		

		elif wrongButtonPress6==False and btnPressed==False:
			print("Wrong button pressed")
			running = False
			gameWon = False
			Thread(target=playSound,daemon=True).start()
			break		

		elif wrongButtonPress7==False and btnPressed==False:
			print("Wrong button pressed")
			running = False
			gameWon = False
			Thread(target=playSound,daemon=True).start()
			break		

		elif wrongButtonPress8==False and btnPressed==False:
			print("Wrong button pressed")
			running = False
			gameWon = False
			Thread(target=playSound,daemon=True).start()
			break		

		elif wrongButtonPress9==False and btnPressed==False:
			print("Wrong button pressed")
			running = False
			gameWon = False
			Thread(target=playSound,daemon=True).start()
			break

		elif wrongButtonPress10==False and btnPressed==False:
			print("Wrong button pressed")
			running = False
			gameWon = False
			Thread(target=playSound,daemon=True).start()
			break

		

	gameComplete = True
	print("GAME OVER",score, gameWon)
	screen4.ShowScreen(pg,screen,score)
		
def switchOffAll():
	for i in allLeds:
		GPIO.output(i,GPIO.LOW)


def generateMapping():	
	random.shuffle(allLeds)
	random.shuffle(allPushBtns)
