#IMPORTS
import pygame
import sys
sys.path.append(".")
from Node import Node
import math
import time
pygame.init()
pygame.font.init()


# VARIABLES
height = 600
width = 800
screen = pygame.display.set_mode((width, height+100))
icon = pygame.image.load("cursor.png")
startSelected = False
endSelected = False
grid = []
gameRunning = True
myfont = pygame.font.SysFont('Arial', 24)
message = myfont.render('', True, (0, 0, 0))
currentNode = None
endRow = None
endCol = None
started = False
finished = False
alt = True


# FUNCTIONS
def setupGrid():
	# Add Columns and Rows to the grid
	for row in range(height // 20):
		newRow = []
		for column in range (width // 20):
			newRow.append(Node(False, False, False, row, column))
		grid.append(newRow)
def setupScreenInfo():
	pygame.display.set_caption("Pathfinder")
	pygame.display.set_icon(icon)
def drawScreen():
	# background color
	global alt
	global finished
	global started
	if started == False:
		screen.fill((200, 200, 200))
	elif finished == True:
		screen.fill((200, 200, 200))
	elif alt == True:
		screen.fill((200, 200, 200))
		alt = False
	elif alt == False:
		screen.fill((235, 235, 235))
		alt = True
	# Fill in the Nodes with Color
	for row in range(height // 20):
		for column in range (width // 20):
			if grid[row][column].isStart == True:
				pygame.draw.rect(screen,(0, 46, 115),(column*20,row*20,20,20))
			elif grid[row][column].isEnd == True:
				pygame.draw.rect(screen,(0, 201, 34),(column*20,row*20,20,20))
			elif grid[row][column].isVisited == True and grid[row][column].isBest == False:
				pygame.draw.rect(screen,(138, 245, 255),(column*20,row*20,20,20))
			elif grid[row][column].isBest == True:
				pygame.draw.rect(screen,(227, 55, 43),(column*20,row*20,20,20))
	# draw the lines that create square nodes
	for row in range((height // 20)+1):
		pygame.draw.line(screen, (0, 0, 0), (0, row*20), (width, row*20))
	for column in range((width // 20)+1):
		pygame.draw.line(screen, (0, 0, 0), (column*20, 0), (column*20, height))
	# User Messages
	global message
	if startSelected == False:
		message = myfont.render('Click to Select a Starting Node', True, (0, 0, 0))
	elif endSelected == False:
		message = myfont.render('Click to Select an Ending Node', True, (0, 0, 0))
	if startSelected == True and endSelected == True:
		message = myfont.render('Press Space to Visualize the Algorithm...', True, (0, 0, 0))
	if started == True and finished == False:
		message = myfont.render('Calculating the shortest Path...', True, (0, 0, 0))
	if finished == True:
		message = myfont.render('The Algorithm has finished!', True, (0, 0, 0))
	screen.blit(message,(255,635))
	# update screen
	pygame.display.update()
def checkForEvents():
	for event in pygame.event.get():
		# Check if the window has been closed
		# Editing the global variable gameRunning
		global gameRunning
		if event.type == pygame.QUIT:
			gameRunning = False
		# Mark down the starting block when the mouse is clicked
		# Make sure that the global version of startSelected is being accessed
		global startSelected
		global endSelected
		global currentNode
		global endRow
		global endCol
		global finished
		global started
		if pygame.mouse.get_pressed() == (True, False, False) and startSelected == False:
			startPos = pygame.mouse.get_pos()
			grid[startPos[1] // 20][startPos[0] // 20].isStart = True
			grid[startPos[1] // 20][startPos[0] // 20].distanceToNode = 0
			currentNode = grid[startPos[1] // 20][startPos[0] // 20]
			startSelected = True
		elif pygame.mouse.get_pressed() == (True, False, False) and endSelected == False:
			endPos = pygame.mouse.get_pos()
			grid[endPos[1] // 20][endPos[0] // 20].isEnd = True
			endRow = endPos[1] // 20
			endCol = endPos[0] // 20
			endSelected = True	
		if event.type == pygame.KEYDOWN and endSelected:
			if event.key == pygame.K_SPACE and started == False:
				started = True
				while finished == False:
					if currentNode.isEnd == True:
						finished = True
						break
					checkAdjacentNodes()
					drawScreen()
def checkAdjacentNodes():
	time.sleep(.5)
	global currentNode
	global endRow
	global endCol
	global grid
	global finished
	row = currentNode.gridRow
	col = currentNode.gridColumn
	up = 999
	down = 999
	left = 999 
	right = 999
	upRight = 999
	upLeft = 999
	downRight = 999
	downLeft = 999
	# Use distance formula with surrounding nodes to find the best one
	if row-1 >= 0:
		up = math.sqrt( (endRow-(row-1))**2 + (endCol-col)**2 )
		grid[row-1][col].isVisited = True
	if row+1 <= height//20-1:
		down = math.sqrt( (endRow-(row+1))**2 + (endCol-col)**2 )
		grid[row+1][col].isVisited = True
	if col-1 >= 0:
		left = math.sqrt( (endRow-row)**2 + (endCol-(col-1))**2)
		grid[row][col-1].isVisited = True
	if col+1 <= width//20-1:
		right = math.sqrt( (endRow-row)**2 + (endCol-(col+1))**2)
		grid[row][col+1].isVisited = True
	
	lowestDistance = 999
	bestNode = None
	if up < down and up < left and up < right:
		bestNode = grid[row-1][col]
	if down < up and down < left and down < right:
		bestNode = grid[row+1][col]
	if left < up and left < down and left < right:
		bestNode = grid[row][col-1]
	if right < up and right <left and right < down:
		bestNode = grid[row][col+1]
	if up == right and up < down:
		bestNode = grid[row-1][col+1]
	if up == left and up <down:
		bestNode = grid[row-1][col-1]
	if down == right and down < up:
		bestNode = grid[row+1][col+1]
	if down == left and down <up:
		bestNode = grid[row+1][col-1]
	currentNode = bestNode
	currentNode.isBest = True

setupGrid()
setupScreenInfo()
#Game Loop
while gameRunning:
	checkForEvents()
	drawScreen()
