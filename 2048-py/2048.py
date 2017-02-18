# 2048 
# J Pearson, 2015
# needs pygame; if not installed, see
# http://juliaelman.com/blog/2013/04/02/installing-pygame-on-osx-mountain-lion/

import pygame, sys, random, func
from pygame.locals import *
import math, colourcodes 
from math import *

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

# Settings for the tiles
# How many tiles in each direction?
nx = 6
ny = 6
ntiles = (nx, ny)
totntiles = nx * ny
TILE_SPACING = 5
TILE_SIZE_X = int( BOARD_WIDTH  / ntiles[0] - ntiles[0] * TILE_SPACING )
TILE_SIZE_Y = int( BOARD_HEIGHT / ntiles[1] - ntiles[1] * TILE_SPACING )
TILE_BG = colourcodes.BLUE

# What is the blank tile coloured?
BLANKTILE_BG_COLOUR = colourcodes.GREY
BLANKTILE_VAL = 0
BLANKTILE_TXT = ""

TXT_2 = "2"
TXT_4 = "4"
TXT_8 = "8"
TXT_16 = "16"
TXT_32 = "32"
TXT_64 = "64"
TXT_128 = "128"
TXT_LIST = (BLANKTILE_TXT, TXT_2, TXT_4, TXT_8, TXT_16, TXT_32, TXT_64, TXT_128)


# Start-up pygame & seed random number generator
pygame.init()
random.seed()

# Print board onto screen
BOARD_DIMS = (BOARD_TOP_X, BOARD_TOP_Y, BOARD_WIDTH, BOARD_HEIGHT)
BG = pygame.display.set_mode((WINDOW_SIZE_X, WINDOW_SIZE_Y), 0, 32)
BG_COLOUR = colourcodes.WHITE
BOARD_COLOUR = colourcodes.BLACK
pygame.display.set_caption('2048')
		
        


# Get a vector containing the available colours
COLOURS = (colourcodes.BLUE, colourcodes.RED, colourcodes.GREEN)


        
def modifyTile(BG, Tiles, tileID, colourID, newVal):
    
    # Set the colour of this random tile
    Tiles[ tileID ].setCol(colourID)
    
    # Specify this tile as being "full", rather than empty
    Tiles[tileID].setFull()
    
    # Change the value of this tile
    Tiles[tileID].setVal( newVal )
    if newVal == BLANKTILE_VAL:
        Tiles[tileID].setEmpty()
        
    # Get the location on the board of this randomly chosen tile
    tl = Tiles[tileID].getLoc()
    
    # Modify the board accordingly
    pygame.draw.rect(BG, Tiles[tileID].getCol(), [tl[0], tl[1], TILE_SIZE_X, TILE_SIZE_Y])
    
    # Modify the text on the given tile
    Tiles[tileID].setTxt( TXT_LIST[ newVal ] )
    # Font of the tile text
    TILE_TEXT_FONT = "monospace"
    TILE_TEXT_FONT_SIZE = 20
    # Padding of the tile text
    TILE_TEXT_PADDING = 10
    TILE_TEXT_POS_X = tl[0] + TILE_TEXT_PADDING
    TILE_TEXT_POS_Y = tl[1] + TILE_TEXT_PADDING
    myfont = pygame.font.SysFont(TILE_TEXT_FONT, TILE_TEXT_FONT_SIZE)
    TILE_LABEL = myfont.render( Tiles[tileID].getTxt(), 1, colourcodes.BLACK )
    BG.blit( TILE_LABEL, ( TILE_TEXT_POS_X, TILE_TEXT_POS_Y ) )            
  #  pygame.display.update()

    
def existsemptytiles(tiles):

# function to return whether there exists any empty tiles or not
    
    n = 0
    
    for i in xrange(0, len(tiles)):
        if tiles[i].isEmpty():
            n = n + 1
            
    if n > 0:
        ret = True
    else:
        ret = False
                
    return ret





BG.fill(BG_COLOUR)
pygame.draw.rect(BG, BOARD_COLOUR, BOARD_DIMS)

# Create an aray of tiles
GameTiles = []

class TILE:
    def __init__(self):
    	self.count = 1

    def setID(self, ID):
    	self.tileID = ID

    def setCol(self, colselect):
    	self.col = colselect

    def setLoc(self, x):
    	self.loc = x  

    def setVal(self, x):
        self.val = x    

    def setTxt(self, x):
        self.txt = x    

    def getLoc(self):
    	return self.loc

    def getVal(self):
        return self.val    

    def getTxt(self):
        return self.txt    

    def getCol(self):
    	return self.col

    def setFull(self):
    	self.EMPTY = False

    def setEmpty(self):
    	self.EMPTY = True
    
    def isEmpty(self):
    	if self.EMPTY:
    		return True
    	else:
    		return False


def killTile(Tiles, ID):
    Tiles[ ID ].setEmpty()
    Tiles[ ID ].setCol( BLANKTILE_BG_COLOUR )
    Tiles[ ID ].setVal( BLANKTILE_VAL )
    Tiles[ ID ].setTxt( BLANKTILE_TXT )

def DoCombine(Tiles, tileID_this, tileID_next, KEYID):
    
   # if KEYID == pygame.K_UP or KEYID == pygame.K_LEFT:
    if not Tiles[ tileID_this ].isEmpty() and not Tiles[ tileID_next ].isEmpty():
        if Tiles[tileID_this].getVal() == Tiles[tileID_next].getVal():
            modifyTile( BG, Tiles, tileID_this, Tiles[ tileID_this ].getCol() ,  Tiles[tileID_this].getVal() + 1 )
            killTile(Tiles, tileID_next)
                
  #  if KEYID == pygame.K_DOWN or KEYID == pygame.K_RIGHT:
  #      if not Tiles[ tileID_this ].isEmpty() and not Tiles[ tileID_next ].isEmpty():
  #          if Tiles[tileID_this].getVal() == Tiles[tileID_next].getVal():
  #              modifyTile( BG, Tiles, tileID_this, Tiles[ tileID_this ].getCol() ,  Tiles[tileID_this].getVal() + 1 )
  #              killTile(Tiles, tileID_next)                


def DoReplace(Tiles, tileID_this, tileID_next):
    modifyTile( BG, Tiles, tileID_next, Tiles[ tileID_this ].getCol() , Tiles[tileID_this].getVal() )
    modifyTile( BG, Tiles, tileID_this, BLANKTILE_BG_COLOUR, BLANKTILE_VAL)
    killTile( Tiles, tileID_this )

def GetInBoard(i, bound, type):
    if type == 1:
        if i > bound:
            return True
        else:
            return False
    if type == 2:
        if i < bound:
            return True
        else:
            return False  

def DoShuffle(Tiles, tileID_this, tileID_next, i, j, dirn, bound):
    
    KEYID = 2

    if dirn[KEYID] == pygame.K_UP or dirn[KEYID] == pygame.K_LEFT:
        DirnType = 1
    if dirn[KEYID] == pygame.K_DOWN or dirn[KEYID] == pygame.K_RIGHT:
        DirnType = 2
    
    while GetInBoard(i, bound, DirnType) and GetInBoard(j, bound, DirnType) and Tiles[ tileID_next ].isEmpty() and not Tiles[ tileID_this ].isEmpty():
        DoReplace(Tiles, tileID_this, tileID_next)
        if i + 2 * dirn[0] > bound and j + 2 * dirn[1] > bound:
            i = i + dirn[0]
            j = j + dirn[1]
            tileID_this = func.getind( i, nx, j, ny)
            tileID_next = func.getind( i + dirn[0], nx, j + dirn[1], ny)
        else:
            break
                             
                

def Shuffle(Tiles,i,j,nx,ny,dirn,bound):
    tileID_this = func.getind( i, nx, j, ny)
    tileID_next = func.getind( i + dirn[0], nx, j + dirn[1], ny)
    DoShuffle(Tiles, tileID_this, tileID_next, i, j, dirn, bound)

def Combine(Tiles,i,j,nx,ny,dirn):
    tileID_this = func.getind( i, nx, j, ny)
    tileID_next = func.getind( i + dirn[0], nx, j + dirn[1], ny)
    DoCombine(Tiles, tileID_this, tileID_next, dirn[2])

def DoMove(keyPRESS):
    
    if keyPRESS == pygame.K_UP:
        dirn = (0, -1, keyPRESS)
        bound = -1
        rang_bound = (0, 1)
        act_s = 0
        act_m = 1
        for i in xrange(rang_bound[act_s], ntiles[act_s]):
            # 1: shuffle up
            for j in xrange(rang_bound[act_m], ntiles[act_m]):
                Shuffle(GameTiles,i,j,nx,ny,dirn,bound)
                         
            # 2: combine like tiles        
            for j in xrange(rang_bound[act_m], ntiles[act_m]):
                Combine(GameTiles,i,j,nx,ny,dirn)
                        
            # 3: shuffle up
            for j in xrange(rang_bound[act_m], ntiles[act_m]):
               Shuffle(GameTiles,i,j,nx,ny,dirn,bound)
                               
                               
    if keyPRESS == pygame.K_LEFT:
        dirn = (-1, 0, keyPRESS)
        bound = -1
        rang_bound = (1, 0)
        act_s = 1
        act_m = 0
        
        for j in xrange(rang_bound[act_s], ntiles[act_s]):
            # 1: shuffle left
            for i in xrange(rang_bound[act_m], ntiles[act_m]):
                Shuffle(GameTiles,i,j,nx,ny,dirn,bound)
                         
            # 2: combine like tiles        
            for i in xrange(rang_bound[act_m], ntiles[act_m]):
                Combine(GameTiles,i,j,nx,ny,dirn)
                        
            # 3: shuffle left
            for i in xrange(rang_bound[act_m], ntiles[act_m]):
                Shuffle(GameTiles,i,j,nx,ny,dirn,bound)   
                                          
    if keyPRESS == pygame.K_RIGHT:
        dirn = (1, 0, keyPRESS)
        act_s = 1
        act_m = 0
        bound = ntiles[act_m]
        rang_bound = (0, 0)
        
        for j in xrange(rang_bound[act_s], ntiles[act_s]):
            # 1: shuffle 
            for i in xrange(rang_bound[act_m], ntiles[act_m]-1):
                Shuffle(GameTiles,i,j,nx,ny,dirn,bound)
                         
            # 2: combine like tiles        
            for i in xrange(rang_bound[act_m], ntiles[act_m]-1):
                Combine(GameTiles,i,j,nx,ny,dirn)
                        
            # 3: shuffle  
            for i in xrange(rang_bound[act_m], ntiles[act_m]-1):
                Shuffle(GameTiles,i,j,nx,ny,dirn,bound)   

    if keyPRESS == pygame.K_DOWN:
        dirn = (0, 1, keyPRESS)
        act_s = 0
        act_m = 1
        bound = ntiles[act_m]
        rang_bound = (0, 0)
        
        
        for i in xrange(rang_bound[act_s], ntiles[act_s]):
            # 1: shuffle 
            for j in xrange(rang_bound[act_m], ntiles[act_m]-1):
                Shuffle(GameTiles,i,j,nx,ny,dirn,bound)
                         
            # 2: combine like tiles        
            for j in xrange(rang_bound[act_m], ntiles[act_m]-1):
                Combine(GameTiles,i,j,nx,ny,dirn)
                        
            # 3: shuffle  
            for j in xrange(rang_bound[act_m], ntiles[act_m]-1):
                Shuffle(GameTiles,i,j,nx,ny,dirn,bound)   
                                                          
   # pygame.display.update()                   
                       


# BEGIN: gameover script         
def itsgameover():
            
    GAMEOVER_FONT_SIZE = 40   
    GAMEOVER_BLINK_FPS = 5         
    GAMEOVER_MAIN_MESSAGE = "Game Over"
    GAMEOVER_MAIN_MESSAGE_POS_X = BOARD_TOP_X
    GAMEOVER_MAIN_MESSAGE_POS_Y = MARGIN_TOP / 3
    GAMEOVER_FONT = "monospace"
    
    myfont = pygame.font.SysFont(GAMEOVER_FONT, GAMEOVER_FONT_SIZE)            
    GAMEOVER_MAIN_MESSAGE_POS = (GAMEOVER_MAIN_MESSAGE_POS_X, GAMEOVER_MAIN_MESSAGE_POS_Y)            

    def GAMEOVER_label( MSG_COL ):
        GAMEOVER_LABEL = myfont.render( GAMEOVER_MAIN_MESSAGE, 1, MSG_COL )
        BG.blit( GAMEOVER_LABEL, GAMEOVER_MAIN_MESSAGE_POS )            
        pygame.display.update()
    
    GOClock = pygame.time.Clock() 

    n = 0
    while True:
       
        for event in pygame.event.get():
            
            if event.type == QUIT:
                print "Game over"  
                pygame.quit()
                sys.exit()
                
        GOClock.tick(GAMEOVER_BLINK_FPS)
        if n < 1:
            GAMEOVER_label(colourcodes.RED)
            n = n + 1
        else:
            GAMEOVER_label(colourcodes.BLUE)
            n = 0
      
         
# END: gameover script
def setupboard():
    tileID = 0
    for i in xrange(0, ntiles[0]):
        TILE_POS_X = func.getloc(i, TILE_SPACING, TILE_SIZE_X, BOARD_TOP_X)
        for j in xrange(0, ntiles[1]):
            TILE_POS_Y = func.getloc(j, TILE_SPACING, TILE_SIZE_Y, BOARD_TOP_Y)
            NewTile = TILE()
            NewTile.setID( tileID )
            NewTile.setEmpty()
            NewTile.setCol( BLANKTILE_BG_COLOUR )
            NewTile.setVal( BLANKTILE_VAL )
            NewTile.setTxt( TXT_LIST[0] )
            NewTile.setLoc( ( TILE_POS_X, TILE_POS_Y ) )
            GameTiles.append( NewTile )
            TILE_BG = GameTiles[ tileID ].getCol()
            pygame.draw.rect(BG, TILE_BG, [TILE_POS_X, TILE_POS_Y, TILE_SIZE_X, TILE_SIZE_Y])
            tloc = GameTiles[ tileID ].getLoc()
            tileID = tileID + 1

def getemptytile(Tiles):
    while True:
        emptyTILEid = func.GetRandomTileID(totntiles)
        if GameTiles[ emptyTILEid ].isEmpty():
            break
    return emptyTILEid  

########################################################

setupboard()

# Put a new tile down (this is for testing)
modifyTile(BG, GameTiles, getemptytile( GameTiles ), colourcodes.RED, 1)

# Update the screen
pygame.display.update()


GetKEY_FPS = 10
fpsClock = pygame.time.Clock() 
stillEmptyTiles = True

ValidKeys = (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
while True:    

	for event in pygame.event.get():
        
        # If the "esc"-key is pressed, kill the game    
		if event.type == QUIT or not stillEmptyTiles:
			pygame.quit()
			sys.exit()

        # If an arrow key is pressed, do something.
        # 1. Get the key press    
        if event.type == pygame.KEYDOWN:
            keyPRESSED = True
            DoMove(event.key)   
            pygame.display.update()   
            print event.key
        else:
            keyPRESSED = False   
                 
        if keyPRESSED:
            # If a user has pressed a key (after the users move has been executed), 
            # fill a random tile (which is currently empty) with a new tile.
            # First, check that there exists empty tiles
            stillEmptyTiles = existsemptytiles(GameTiles)
            if stillEmptyTiles:

                NewTileID = getemptytile( GameTiles )
                # Now modify that empty tile    
                #NewTileBG = COLOURS[random.randint(0, len(COLOURS) - 1 ) ]
                NewTileBG = COLOURS[1]
                NewTileTXT = TXT_LIST[1]
                modifyTile(BG, GameTiles, NewTileID, NewTileBG , 1 )
            
            # Update the game screen
            pygame.display.update()        
        
        # If there are no spare places left to put a tile,
        # break out of the game; otherwise, keep running
        if not stillEmptyTiles:
            break
        else:
            fpsClock.tick(GetKEY_FPS)	                

itsgameover()
