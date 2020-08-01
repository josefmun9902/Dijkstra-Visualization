#IMPORTS
import pygame
import sys
sys.path.append(".")
from Node import Node
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


# FUNCTIONS
def setupGrid():
	# Add Columns and Rows to the grid
	for row in range(height // 20):
		newRow = []
		for column in range (width // 20):
			newRow.append(Node(False, False, False))
		grid.append(newRow)
def setupScreenInfo():
	pygame.display.set_caption("Pathfinder")
	pygame.display.set_icon(icon)
def drawScreen():
	# background color
	screen.fill((255, 255, 255))
	# Fill in the Nodes with Color
	for row in range(height // 20):
		for column in range (width // 20):
			if grid[row][column].isStart == True:
				pygame.draw.rect(screen,(0, 46, 115),(column*20,row*20,20,20))
			elif grid[row][column].isEnd == True:
				pygame.draw.rect(screen,(0, 201, 34),(column*20,row*20,20,20))
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
		message = myfont.render('', True, (0, 0, 0))
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
		if pygame.mouse.get_pressed() == (True, False, False) and startSelected == False:
			startPos = pygame.mouse.get_pos()
			grid[startPos[1] // 20][startPos[0] // 20].isStart = True
			startSelected = True
		elif pygame.mouse.get_pressed() == (True, False, False) and endSelected == False:
			endPos = pygame.mouse.get_pos()
			grid[endPos[1] // 20][endPos[0] // 20].isEnd = True
			endSelected = True			


setupGrid()
setupScreenInfo()
#Game Loop
while gameRunning:
	checkForEvents()
	drawScreen()