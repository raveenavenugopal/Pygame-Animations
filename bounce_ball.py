import pygame, sys
import time
from pygame import gfxdraw
from pygame.locals import *


red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

pygame.init()

def font():
	font=pygame.font.Font(None,50)
	text=font.render("Bouncing Ball",True,blue,white)
	text_rect=text.get_rect()
	text_rect.centery=50
	screen.blit(text,text_rect)


screen = pygame.display.set_mode((640, 570))
clock = pygame.time.Clock()

screen.fill((255,255,255))
posx=320
posy=170
flag=1

while 1:
	screen.fill((255,255,255))
	font()
   	color = (100,55,130)
	if flag==0:
		posy=posy-1
		if posy<=95:
			flag=1
	else:
		posy = posy+1
		if posy >=475 :
			flag=0
	
	pygame.draw.line(screen,green,(0,70),(640,70),3)
	pygame.draw.line(screen,green,(0,500),(640,500),3)
	pygame.draw.circle(screen, color, (posx,posy), 25)
	pygame.display.update()	
	clock.tick(150)

	for event in pygame.event.get():
        	if event.type==pygame.QUIT:sys.exit()
	
	


