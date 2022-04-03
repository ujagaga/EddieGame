import json

leaderBoard = []


def updateScores(username,points):
	username = username.replace("\r","")
	username = username.strip()
	filePath = "media/scorecard.json"

	f = open(filePath)
	data = json.load(f)
	f.close()

	newData = {
		"user": username,
		"points": points
	}

	data.append(newData)

	g = open(filePath,"w")
	json.dump(data,g)
	g.close()

def prepareLeaderboard():
	global leaderBoard

	filePath = "media/scorecard.json"
	f = open(filePath)
	data = json.load(f)
	f.close()
	
	scoresList = []

	for user in data:
		scoresList.append(user)

	scoresList.sort(key=lambda k:k['points'],reverse=True)	

	if len(scoresList) <= 10:
		leaderBoard = scoresList
	else:
		leaderBoard = scoresList[:10]	

def ShowScreen(pg,screen):
	x,y = screen.get_size()

	image = pg.image.load("media/leaderboard.png")
	image = pg.transform.scale(image, (x, y))

	screen.blit(image,(0,0))
	


	# LIST 1 ------------------------
	
	base = 0
	
	firstRect = pg.Rect(base + (x//25), (y//7),x//12,x//12)
	pg.draw.rect(screen, (255,0,0), firstRect)

	nameRect = pg.Rect(base+(x//25)+(x//12),(y//7),x//4,x//12)
	pg.draw.rect(screen, (0,0,0), nameRect)

	scoreRect = pg.Rect(base+(x//25)+(x//12)+(x//4),(y//7),x//12,x//12)
	pg.draw.rect(screen, (0,255,0), scoreRect)

	try:
		player = leaderBoard[0]
		playerName = player['user']
		playerPoints = player['points']


		fontSize = x//14

		textObj = pg.font.Font('freesansbold.ttf',fontSize)
		textObj2 = pg.font.Font('freesansbold.ttf',fontSize//2)

		text_surface1 = textObj.render("1", True, (255,255,255))
		screen.blit(text_surface1, (firstRect.x+(firstRect.x //2), firstRect.y+5))
		
		text_surface2 = textObj2.render(playerName, True, (255,255,255))
		# screen.blit(text_surface2, (nameRect.x+(firstRect.x //2), nameRect.y+(nameRect.y//2 - fontSize//2)))
		screen.blit(text_surface2, (nameRect.x+(firstRect.x //2), nameRect.y+(fontSize//4)))
		
		if playerPoints >=10:

			playerPoints = str(playerPoints)
			text_surface3 = textObj.render(playerPoints, True, (255,255,255))
			screen.blit(text_surface3, (scoreRect.x+5, scoreRect.y+5))

		else:
			playerPoints = str(playerPoints)
			text_surface3 = textObj.render(playerPoints, True, (255,255,255))
			screen.blit(text_surface3, (scoreRect.x+(firstRect.x//2), scoreRect.y+5))
				
	
	except:
		pass

	for i in range(1,5):
		rect = pg.Rect(base+(x//25), (y//7)+((y//7)*i)+((y//35)*i),x//12,x//12)
		pg.draw.rect(screen, (255,0,0), rect)

		rect2 = pg.Rect(base+(x//25)+(x//12),(y//7)+((y//7)*i)+((y//35)*i),x//4,x//12)
		pg.draw.rect(screen, (0,0,0), rect2)

		rect3 = pg.Rect(base+(x//25)+(x//12)+(x//4),(y//7)+((y//7)*i)+((y//35)*i),x//12,x//12)
		pg.draw.rect(screen, (0,255,0), rect3)

		try:
			player = leaderBoard[i]
			playerName = player['user']
			playerPoints = player['points']

			fontSize = x//14

			textObj = pg.font.Font('freesansbold.ttf',fontSize)
			textObj2 = pg.font.Font('freesansbold.ttf',fontSize//2)

			text_surface1 = textObj.render(str(i+1), True, (255,255,255))
			screen.blit(text_surface1, (rect.x+(rect.x //2), rect.y+5))
			
			text_surface2 = textObj2.render(playerName, True, (255,255,255))
			# screen.blit(text_surface2, (rect2.x+(rect.x //2), rect2.y+(rect2.y//2 - fontSize//2)))
			# screen.blit(text_surface2, (rect2.x+(rect.x //2), rect2.y+5))
			screen.blit(text_surface2, (rect2.x+(rect.x //2), rect2.y+(fontSize//4)))
			
			if playerPoints >=10:

				playerPoints = str(playerPoints)
				text_surface3 = textObj.render(playerPoints, True, (255,255,255))
				screen.blit(text_surface3, (rect3.x+5, rect3.y+5))

			else:
				playerPoints = str(playerPoints)
				text_surface3 = textObj.render(playerPoints, True, (255,255,255))
				screen.blit(text_surface3, (rect3.x+(rect.x//2), rect3.y+5))
					
		
		except Exception as e:
			print(e)
			pass

	# LIST 2 -------------------------


	base = (x//25)+(x//12)+(x//4)+(x//12)+(x//25)
	
	firstRect = pg.Rect(base + (x//25), (y//7),x//12,x//12)
	pg.draw.rect(screen, (255,0,0), firstRect)

	nameRect = pg.Rect(base+(x//25)+(x//12),(y//7),x//4,x//12)
	pg.draw.rect(screen, (0,0,0), nameRect)

	scoreRect = pg.Rect(base+(x//25)+(x//12)+(x//4),(y//7),x//12,x//12)
	pg.draw.rect(screen, (0,255,0), scoreRect)

	try:
		player = leaderBoard[5]
		playerName = player['user']
		playerPoints = player['points']

		print(playerPoints)
		fontSize = x//14

		textObj = pg.font.Font('freesansbold.ttf',fontSize)
		textObj2 = pg.font.Font('freesansbold.ttf',fontSize//2)

		text_surface1 = textObj.render("6", True, (255,255,255))
		# screen.blit(text_surface1, (firstRect.x+(firstRect.x //2), firstRect.y+5))
		screen.blit(text_surface1, (firstRect.x+(x//48), firstRect.y+5))
		
		text_surface2 = textObj2.render(playerName, True, (255,255,255))
		# screen.blit(text_surface2, (nameRect.x+(firstRect.x //2), nameRect.y+(fontSize//4)))
		screen.blit(text_surface2, (nameRect.x+(x//48), nameRect.y+(fontSize//4)))
		
		if playerPoints >=10:

			playerPoints = str(playerPoints)
			text_surface3 = textObj.render(playerPoints, True, (255,255,255))
			screen.blit(text_surface3, (scoreRect.x+5, scoreRect.y+5))

		else:
			playerPoints = str(playerPoints)
			text_surface3 = textObj.render(playerPoints, True, (255,255,255))
			# screen.blit(text_surface3, (scoreRect.x+(firstRect.x//2), scoreRect.y+5))
			screen.blit(text_surface3, (scoreRect.x+(x//48), scoreRect.y+5))
				
	
	except:
		pass

	for i in range(1,5):
		rect = pg.Rect(base+(x//25), (y//7)+((y//7)*i)+((y//35)*i),x//12,x//12)
		pg.draw.rect(screen, (255,0,0), rect)

		rect2 = pg.Rect(base+(x//25)+(x//12),(y//7)+((y//7)*i)+((y//35)*i),x//4,x//12)
		pg.draw.rect(screen, (0,0,0), rect2)

		rect3 = pg.Rect(base+(x//25)+(x//12)+(x//4),(y//7)+((y//7)*i)+((y//35)*i),x//12,x//12)
		pg.draw.rect(screen, (0,255,0), rect3)

		try:
			player = leaderBoard[5+i]
			playerName = player['user']
			playerPoints = player['points']

			fontSize = x//14

			textObj = pg.font.Font('freesansbold.ttf',fontSize)
			textObj2 = pg.font.Font('freesansbold.ttf',fontSize//2)

			if i+6 >=10:
				text_surface1 = textObj.render(str(i+6), True, (255,255,255))
				screen.blit(text_surface1, (rect.x+5, rect.y+5))
			else:	
				text_surface1 = textObj.render(str(i+6), True, (255,255,255))
				screen.blit(text_surface1, (rect.x+(x//48), rect.y+5))
			
			text_surface2 = textObj2.render(playerName, True, (255,255,255))
			# screen.blit(text_surface2, (rect2.x+(rect.x //2), rect2.y+(rect2.y//2 - fontSize//2)))
			# screen.blit(text_surface2, (rect2.x+(rect.x //2), rect2.y+5))
			screen.blit(text_surface2, (rect2.x+(x //48), rect2.y+(fontSize//4)))
			
			if playerPoints >=10:

				playerPoints = str(playerPoints)
				text_surface3 = textObj.render(playerPoints, True, (255,255,255))
				screen.blit(text_surface3, (rect3.x+5, rect3.y+5))

			else:
				playerPoints = str(playerPoints)
				text_surface3 = textObj.render(playerPoints, True, (255,255,255))
				screen.blit(text_surface3, (rect3.x+(x//48), rect3.y+5))
					
		
		except Exception as e:
			print(e)
			pass
	# fontSize = x//20
	# textObj = pg.font.Font('freesansbold.ttf',fontSize)
	# text_surface = textObj.render(f"Game Over", True, (0,0,0))

	# screen.blit(text_surface, (x//10,y//3))

	pg.display.update()