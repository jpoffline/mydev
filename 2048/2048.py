# 2048 

# needs pygame; if not installed, see
# http://juliaelman.com/blog/2013/04/02/installing-pygame-on-osx-mountain-lion/

import pygame, sys, random, colourcodes, func
from pygame.locals import *
from math import *

pygame.init()
random.seed()

class TILE:
	def __init__(self):
		self.count = 1

	def setCol(self,colselect):
		self.COLOUR = colselect
	
	def setLoc(self):
		return 1.0

	def getLoc(self):
		return 1.0

	def getCol(self):
		return self.COLOUR

	def setFull(self):
		self.EMPTY = False

	def setEmpty(self):
		self.EMPTY = True
        
	def isEmpty(self):
		if self.EMPTY:
			return True
		else:
			return False



# Get a vector containing the available colours
COLOURS = (colourcodes.BLUE, colourcodes.RED, colourcodes.GREEN, colourcodes.GREY)

# How many tiles in each direction?
nx = 5
ny = 5
ntiles = (nx, ny)
totntiles = nx * ny

# Dimensions of the game window
WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 500
# size of the margins for the board
MARGIN_TOP = 60
MARGIN_SIDE = 10
MARGIN_BOTTOM = 10

# where is the (x,y)-position of the board, in the window?
BOARD_TOP_X = MARGIN_SIDE
BOARD_TOP_Y = MARGIN_TOP

# Setup width & height of the board
BOARD_WIDTH = WINDOW_SIZE_X - 2 * MARGIN_SIDE
BOARD_HEIGHT = WINDOW_SIZE_Y - MARGIN_TOP - MARGIN_BOTTOM

# Print board onto screen
BOARD_DIMS = (BOARD_TOP_X, BOARD_TOP_Y, BOARD_WIDTH, BOARD_HEIGHT)
BG = pygame.display.set_mode((WINDOW_SIZE_X, WINDOW_SIZE_Y), 0, 32)
BG_COLOUR = colourcodes.WHITE
BOARD_COLOUR = colourcodes.BLACK
pygame.display.set_caption('2048')

TILE_SPACING = 5
TILE_SIZE_X = int( BOARD_WIDTH  / ntiles[0] - ntiles[0] * TILE_SPACING )
TILE_SIZE_Y = int( BOARD_HEIGHT / ntiles[1] - ntiles[1] * TILE_SPACING )
TILE_BG = colourcodes.BLUE


# Create a blank tile
blanktile = TILE()

# What is the blank tile coloured?
BLANKTILE_BG_COLOUR = colourcodes.GREY

blanktile.setCol(BLANKTILE_BG_COLOUR)

# Set the blank tile to be empty
blanktile.setEmpty()

# Create an array of tiles
GameTiles = []

# Loop over all tiles needed for the game
# and set them up: empty & location
for i in xrange(0, totntiles):
    
    # Create a new tile
	NewTile = TILE()
    
    # Make the tile blank
	NewTile = blanktile
	
    # Put this new tile onto the array of all tiles    
	GameTiles.append(blanktile)



BG.fill(BG_COLOUR)
pygame.draw.rect(BG, BOARD_COLOUR, BOARD_DIMS)

print len(GameTiles)


for i in xrange(0, ntiles[0]):
	TILE_POS_X = func.getloc(i, TILE_SPACING, TILE_SIZE_X, BOARD_TOP_X)
	for j in xrange(0, ntiles[1]):
		TILE_POS_Y = func.getloc(j, TILE_SPACING, TILE_SIZE_Y, BOARD_TOP_Y)	
		TILE_BG = GameTiles[ func.getind(i,nx,j,ny) ].getCol()
		pygame.draw.rect(BG, TILE_BG, [TILE_POS_X, TILE_POS_Y, TILE_SIZE_X, TILE_SIZE_Y])


# Get the ID for a random tile
RandomTILE = func.GetRandomTileID(totntiles)


print RandomTILE
# Set the colour
GameTiles[ RandomTILE ].setCol(colourcodes.BLUE)


for i in xrange(0, ntiles[0]):
	TILE_POS_X = func.getloc(i, TILE_SPACING, TILE_SIZE_X, BOARD_TOP_X)
	for j in xrange(0, ntiles[1]):
		TILE_POS_Y = func.getloc(j, TILE_SPACING, TILE_SIZE_Y, BOARD_TOP_Y)	
		TILE_BG = GameTiles[ func.getind(i,nx,j,ny) ].getCol()
		pygame.draw.rect(BG, TILE_BG, [TILE_POS_X, TILE_POS_Y, TILE_SIZE_X, TILE_SIZE_Y])
        
while True:    
    
    
    
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()



	