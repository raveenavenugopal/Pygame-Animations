import pygame,sys
import random
from pygame import *
import math
 
 
black = [0,0,0]
white = [255,255,255]
color = [0,100,100] 
darkBlue=[0,0,120]
red=[120,2,2]
pink = (255,220,200)
blue=[120,20,255]
sky=[0,200,200]
grey=[124,124,124]
green=[0,255,0]
SIZE = [500, 480]
count=0
a1=200
b1=300
wl=418
vl=1
flag=0

inc=265
count1=0

pygame.init()

def font():
	font=pygame.font.Font(None,50)
	text=font.render("Tap & Water",True,white)
	text_rect=text.get_rect()
	text_rect.centery=50
	screen.blit(text,text_rect)

wlist = []
vlist= []

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Water")
clock = pygame.time.Clock()


for i in range(100):
	x=168
	y=265
	wlist.append([x,y])

for i in range(10):
	x=205
	y=350
	vlist.append([x,y])


while 1:
	screen.fill(black)
	font()

	pygame.draw.line(screen,pink,[0,420],[500,420],3)
	pygame.draw.line(screen,pink,[105,420],[105,250],3)
	pygame.draw.line(screen,pink,[100,420],[100,250],3)
	pygame.draw.line(screen,pink,[100,250],[150,250],3)
	pygame.draw.line(screen,pink,[105,255],[150,255],3)
	pygame.draw.ellipse(screen,white,[150,240,20,10])
	pygame.draw.line(screen,red,[150,250],[170,250],2)
	pygame.draw.line(screen,grey,[150,255],[165,255],2)
	pygame.draw.line(screen,grey,[170,250],[170,265],2)
	pygame.draw.line(screen,grey,[165,255],[165,265],2)
	pygame.draw.line(screen,green,[130,420],[130,347],2)
	pygame.draw.line(screen,green,[200,420],[200,347],2)
	pygame.draw.line(screen,green,[130,418],[200,418],2)
	
	a=math.radians(a1)
	b=math.radians(b1)
	pygame.draw.rect(screen,sky,[132,wl,68,vl])

	for i in range(len(wlist)):
		pygame.draw.circle(screen,sky,wlist[i],2)
		wlist[i][1] += 1
		if wlist[i][1] > 415:
			count+=1
			y =random.randrange(265,365)
			wlist[i][1] = y

	if count>=12 and flag==0:
		wl-=1
		vl+=1
		count=0
		if wl<350:
			flag=1
	if flag==1:
		for i in range(len(vlist)):
			pygame.draw.circle(screen,sky,vlist[i],2)
			vlist[i][1]+=1
			if vlist[i][1]>418:
				y=random.randrange(350,365)
				vlist[i][1]=y

	pygame.draw.line(screen,sky,[167,265],[167,inc],3)
	count1+=1
	if count1>=5 and inc<=410:
		inc+=1
		count=0
	pygame.draw.arc(screen,darkBlue,(130,420,140,110),a,b,3)
	pygame.draw.ellipse(screen,green,[125,340,83,15],2)

	clock.tick(100)
	pygame.display.update()
	
	for event in pygame.event.get():
        	if event.type==pygame.QUIT:
			sys.exit()

