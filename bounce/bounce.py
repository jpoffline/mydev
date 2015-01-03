import pygame, sys, random, math
from pygame.locals import *
pygame.init()
random.seed()

FPS = 100
fpsClock = pygame.time.Clock()

WINDOW_SIZEX = 500
WINDOW_SIZEY = 500

FONT_SIZE = 30

DISPLAYSURF = pygame.display.set_mode((WINDOW_SIZEX, WINDOW_SIZEY), 0, 32)
catIMG = pygame.image.load('cat.png')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


pos_x = int( WINDOW_SIZEX / 2 )
pos_y = int( WINDOW_SIZEY / 2 )

pos = [pos_x, pos_y]
WINDOW_SIZE = [WINDOW_SIZEX, WINDOW_SIZEY]
t = 0
dt = 0.1
t = 0
v_x = 5
v_y = 3
vel = [v_x, v_y]
ndim = 2

while True:
	
	text_col = WHITE
	DISPLAYSURF.fill(BLUE)
	

	posOLD = pos
	for i in range(0, ndim):		
		pos[i] = pos[i] + vel[i]
		posNEW = pos[i] + vel[i]
		if posNEW < 0:
		       	vel[i] = - vel[i]
		if posNEW > WINDOW_SIZE[i]:
		      	vel[i] = - vel[i]
		pos[i] = pos[i] + vel[i]
		
	img_pos = pos		
	myfont = pygame.font.SysFont("monospace", FONT_SIZE)

	# render text
	text_msg = "Hello"  	
	label = myfont.render(text_msg, 1, text_col)
	
	DISPLAYSURF.blit(catIMG, img_pos)
	
		
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	t = t + 1
	pygame.display.update()
	fpsClock.tick(FPS)	
