# import and initialize py game
import pygame
pygame.init()

# set up the screen with dimsensions
height = 600
width = 800
screen = pygame.display.set_mode((width, height+100))

#Title and Icon 
pygame.display.set_caption("Pathfinder")
icon = pygame.image.load("cursor.png")
pygame.display.set_icon(icon)

# Game data
# Create the grid (2D Array)
grid = []
# Add Columns and Rows to the grid
for row in range(height // 20):
	newRow = []
	for column in range (width // 20):
		newRow.append([])
	grid.append(newRow)
# Start and End
startSelected = False
endSelected = False

# variable that tells if the game is running
running = True
#Game Loop
while running:

	#EVENT CHECKS
	for event in pygame.event.get():
		# Check if the window has been closed
		if event.type == pygame.QUIT:
			running = False
		# Mark down the starting block when the mouse is clicked
		if pygame.mouse.get_pressed() == (True, False, False) and startSelected == False:
			startPos = pygame.mouse.get_pos()
			grid[startPos[1] // 20][startPos[0] // 20] = "Start"
			for row in range(height // 20):
				print(grid[row])
			startSelected = True

	#SCREEN DRAWING
	# background color
	screen.fill((255, 255, 255))
	# draw the lines that create square nodes
	for row in range((height // 20)+1):
		pygame.draw.line(screen, (0, 0, 0), (0, row*20), (width, row*20))
	for column in range((width // 20)+1):
		pygame.draw.line(screen, (0, 0, 0), (column*20, 0), (column*20, height))

	# update screen
	pygame.display.update()