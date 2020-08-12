import pygame
import world as w
import numpy as np

world=0#placeholder, set in main.py

'''
showGrid=True
'''
showGrid=False
#'''

tileSize=16
tileTotal=tileSize
if(showGrid):
	tileTotal+=1

#icon = pygame.image.load("snake-clip.png")
#pygame.display.set_icon(icon)
#screen.blit(icon, (50, 50))

#defaults as placeholders, set in renderInit() 
xGridTotal=w.worldX*tileTotal
yGridTotal=w.worldY*tileTotal

'''
sizebartop=50
sizebarbottom=50
sizebarleft=50
sizebarright=50
'''
sizebartop=0
sizebarbottom=0
sizebarleft=0
sizebarright=0
#'''

wc=(sizebarleft,sizebartop)
if(showGrid):
	to=np.add(wc,(1,1))
else:
	to=wc

screenX=xGridTotal+sizebarright+sizebarleft
screenY=yGridTotal+sizebartop+sizebarbottom
if(showGrid):
	screenX+=1
	screenY+=1

#icon = pygame.image.load("snake-clip.png")
#pygame.display.set_icon(icon)
#screen.blit(icon, (50, 50))

font = pygame.font.Font('freesansbold.ttf', 32)

screen=pygame.display.set_mode((screenX, screenY))#placeholder, set in renderInit()

roadImg=pygame.image.load("src/images/clay.png")
wallImg=pygame.image.load("src/images/obsidian.png")

aImg=pygame.image.load("src/images/red_wool.png")
bImg=pygame.image.load("src/images/blue_wool.png")

pathImg=pygame.image.load("src/images/lime_wool.png")
visitedImg=pygame.image.load("src/images/yellow_wool.png")

bgcolor=(50,50,50)
clrwhite=(255, 255, 255)

def renderInit():
	global tileTotal
	global xGridTotal
	global yGridTotal
	global wc
	global to
	global screenX
	global screenY
	global screen
	
	tileTotal=tileSize
	if(showGrid):
		tileTotal+=1
	
	xGridTotal=world.worldX*tileTotal
	yGridTotal=world.worldY*tileTotal
	
	wc=(sizebarleft,sizebartop)
	if(showGrid):
		to=np.add(wc,(1,1))
	else:
		to=wc

	screenX=xGridTotal+sizebarright+sizebarleft
	screenY=yGridTotal+sizebartop+sizebarbottom
	if(showGrid):
		screenX+=1
		screenY+=1
	
	screen = pygame.display.set_mode((screenX, screenY))
	pygame.display.set_caption("Pathfinder")

def renderTiles():
	for x in world.grid:#x is row
		for y in x:#y is tile
			renderTile(y)

def renderTile(t):
	cord=(t.x, t.y)
	cord=np.multiply(tileTotal,cord)
	cord=np.add(to,cord)
	if(t.visited):
		screen.blit(visitedImg, cord)
	elif(t.wall):
		screen.blit(wallImg, cord)
	else:
		screen.blit(roadImg, cord)
	#print(c)

def renderpoints():
	w=world
	cord=(w.a[0], w.a[1])
	cord=np.multiply(tileTotal,cord)
	cord=np.add(to,cord)
	screen.blit(aImg, cord)
	
	cord=(w.b[0], w.b[1])
	cord=np.multiply(tileTotal,cord)
	cord=np.add(to,cord)
	screen.blit(bImg, cord)
	
def renderTick():
	renderTiles()
	renderpoints()
	pygame.display.update()

def renderFirst():
	screen.fill(bgcolor)
	if(showGrid):
		renderGridBorder()
	renderTick()

def renderGridBorder():
	for x in range(world.worldX):
		pygame.draw.line(screen,clrwhite,np.add(wc,(x*tileTotal,0)),np.add(wc,(x*tileTotal,yGridTotal)),1)
	for y in range(world.worldY):
		pygame.draw.line(screen,clrwhite,np.add(wc,(0,y*tileTotal)),np.add(wc,(xGridTotal,y*tileTotal)),1)
	pygame.draw.line(screen,clrwhite,np.add(wc,(0,yGridTotal)),np.add(wc,(xGridTotal,yGridTotal)),1)
	pygame.draw.line(screen,clrwhite,np.add(wc,(xGridTotal,0)),np.add(wc,(xGridTotal,yGridTotal)),1)
	
