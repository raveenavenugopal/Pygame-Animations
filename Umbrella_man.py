import pygame
import random
from pygame import *
from pygame import gfxdraw
import math
 
pygame.init()
 
black = [0,0,0]
white = [255,255,255]
color = [0,100,100] 
darkBlue=[0,0,120]
red=[120,2,2]
pink = (255,220,200)
blue=[120,20,255]
SIZE = [800, 480]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Rain Animation")

rain_list = []
xc=100
yc=280
a1=f=flag=0
b1=180
r=100
h1=h2=90
rr=40
e=55

for i in range(150):
	x = random.randrange(0, 800)
	y = random.randrange(0, 480)
	rain_list.append([x, y])
 
clock = pygame.time.Clock()
 
done = False

while done == False:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done = True 
	screen.fill(white)

	a=math.radians(a1)
	b=math.radians(b1)

	pygame.draw.arc(screen,darkBlue,(e,200,140,110),a,b,3)
	pygame.draw.arc(screen,darkBlue,(e+48,200,45,110),a,b,3)
	pygame.draw.arc(screen,darkBlue,(e+20,200,100,110),a,b,3)

	pygame.draw.arc(screen,darkBlue,(e,248,20,10),a,b,3)
	pygame.draw.arc(screen,darkBlue,(e+20,248,28,10),a,b,3)
	pygame.draw.arc(screen,darkBlue,(e+48,248,42,10),a,b,3)
	pygame.draw.arc(screen,darkBlue,(e+90,248,28,10),a,b,3)
	pygame.draw.arc(screen,darkBlue,(e+118,248,20,10),a,b,3)
	pygame.draw.circle(screen,black,[xc,yc+10],25,2)
	pygame.draw.line(screen,red,[e+70,250],[e+70,325],3)
	pygame.draw.rect(screen,black, [e+68,325,7,7])
	pygame.draw.line(screen,black,[xc,yc+35],[xc,yc+80],3)

	x=int(rr * math.cos(math.radians(h1)))
	y=int(rr * math.sin(math.radians(h1)))
	
	pygame.draw.line(screen,black,[xc,yc+45],[x+xc,y+yc+45],3)
	pygame.draw.line(screen,black,[xc,yc+45],[xc+15,yc+55],3)
	pygame.draw.line(screen,black,[xc+15,yc+55],[xc+25,yc+45],3)
	pygame.draw.rect(screen,red, [0,400,800,80])

	x=int(rr * math.cos(math.radians(h1)))
	y=int(rr * math.sin(math.radians(h1)))
	pygame.draw.line(screen,black,[xc,yc+80],[x+xc,y+yc+80],3)
	x=int(rr * math.cos(math.radians(h2)))
	y=int(rr * math.sin(math.radians(h2)))
	pygame.draw.line(screen,black,[xc,yc+80],[x+xc,y+yc+80],3)
	
	if(h1 >=115 or h2 <=65 ):
		flag=1
	if(h1<=65 or h2 >=115):
		flag=0
	
	pygame.draw.line(screen,black,[0,400],[800,400],10)
	
	if f==0:
		e=e+1
		xc=xc+1
		if xc>=650:
			f=1
	elif f==1:
		e=e-1
		xc=xc-1
		if xc<=50:
			f=0

	if (flag==0):
		h1=(h1+3)%360
		h2=(h2-3)%360
	else:
		h1=(h1-3)%360
		h2=(h2+3)%360

	for i in range(len(rain_list)):
		pygame.draw.circle(screen,black,rain_list[i], 2)
		rain_list[i][1] += 5
	r2=40
	r1=65
	t=3.14/180
	n=80
	while(n<280):
		d=n*t
		z1=int((xc+20)+r1*math.sin(d))
		z2=int((yc-40)+r2*math.cos(d))
		#gfxdraw.pixel(screen,z1,z2,black)
		n+=1
		for j in range(len(rain_list)):
			if rain_list[j][0] >=z1 and rain_list[j][1] >=z2 and rain_list[j][0]<=z1+10:
				y = random.randrange(-50, -10)
				rain_list[j][1] = y
				x = random.randrange(0, 800)
				rain_list[j][0] = x
			if rain_list[j][1] > 400:
				y = random.randrange(-50, -10)
				rain_list[j][1] = y
				x = random.randrange(0, 800)
				rain_list[j][0] = x
			
	pygame.display.update()
	clock.tick(30)
pygame.quit ()

