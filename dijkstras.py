#IMPORTS
import pygame
pygame.init()


# VARIABLES
height = 600
width = 800
screen = pygame.display.set_mode((width, height+100))
icon = pygame.image.load("cursor.png")
startSelected = False
endSelected = False
grid = []
gameRunning = True

# FUNCTIONS
def setupGrid():
	# Add Columns and Rows to the grid
	for row in range(height // 20):
		newRow = []
		for column in range (width // 20):
			newRow.append([])
		grid.append(newRow)
def setupScreenInfo():
	pygame.display.set_caption("Pathfinder")
	pygame.display.set_icon(icon)
def drawScreen():
	# background color
	screen.fill((255, 255, 255))
	# draw the lines that create square nodes
	for row in range((height // 20)+1):
		pygame.draw.line(screen, (0, 0, 0), (0, row*20), (width, row*20))
	for column in range((width // 20)+1):
		pygame.draw.line(screen, (0, 0, 0), (column*20, 0), (column*20, height))
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
		if pygame.mouse.get_pressed() == (True, False, False) and startSelected == False:
			startPos = pygame.mouse.get_pos()
			grid[startPos[1] // 20][startPos[0] // 20] = "Start"
			for row in range(height // 20):
				print(grid[row])
			startSelected = True

setupGrid()
setupScreenInfo()

#Game Loop
while gameRunning:
	checkForEvents()
	drawScreen()