import pygame, sys
import time,math
from pygame import gfxdraw
from pygame.locals import *

color = (100,55,130)
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
	text=font.render("Bicycle",True,blue,white)
	text_rect=text.get_rect()
	text_rect.centery=50
	screen.blit(text,text_rect)

screen = pygame.display.set_mode((840, 480))
screen.fill((255,255,255))
xc1=100
yc1=350
xc2=250
yc2=350
ang=angl=0
r=50
flag=0

clock = pygame.time.Clock()

while 1:
	screen.fill((255,255,255))
	font()
	pygame.draw.circle(screen,black,[xc1,yc1],50,7)
	pygame.draw.circle(screen,black,[xc1,yc1],10)
	pygame.draw.circle(screen,black,[xc2,yc2],50,7)
	pygame.draw.circle(screen,black,[xc2,yc2],10)
	angl=ang
	pygame.draw.line(screen,color,[0,403],[840,403],10)
	
	for i in range(8):
		x=int(r * math.cos(math.radians(angl)))
		y=int(r * math.sin(math.radians(angl)))
		pygame.draw.line(screen,black,[xc1,yc1],[x+xc1,y+yc1],3)
		angl=(angl+45)%360
		
		
	for i in range(8):
		x=int(r * math.cos(math.radians(angl)))
		y=int(r * math.sin(math.radians(angl)))
		pygame.draw.line(screen,black,[xc2,yc2],[x+xc2,y+yc2],3)
		angl=(angl+45)%360
	

	pygame.draw.line(screen,darkBlue,[xc2,yc2],[xc2-20,yc2-60],4)
	pygame.draw.line(screen,darkBlue,[xc2-20,yc2-60],[xc2-120,yc2-60],4)
	pygame.draw.line(screen,darkBlue,[xc2,yc2],[xc2-20,yc2-60],5)
	pygame.draw.line(screen,blue,[xc2-25,yc2-60],[xc2-25,yc2-80],4)
	pygame.draw.circle(screen,black,[xc1+75,yc1],15)
	pygame.draw.line(screen,darkBlue,[xc1,yc1],[xc2-120,yc2-60],4)
	pygame.draw.line(screen,darkBlue,[xc2-120,yc2-60],[xc1+75,yc1],4)
	pygame.draw.line(screen,darkBlue,[xc1+75,yc1],[xc2-20,yc2-60],4)
	pygame.draw.line(screen,black,[xc1,yc1+9],[xc1+75,yc1+14],3)
	pygame.draw.line(screen,black,[xc1,yc1-9],[xc1+75,yc1-14],4)
	pygame.draw.line(screen,black,[xc2-25,yc2-80],[xc2-50,yc2-80],5)
	xc1+=1
	xc2+=1
	ang=(ang+2)%360
	

	pygame.display.update()	
	#time.sleep(0.1)
	clock.tick(20)
	for event in pygame.event.get():
        	if event.type==pygame.QUIT:sys.exit()

