import world as w
import render as r
import pygame

#1000= 1 second
delay=5

world=0#placeholder, set in main.py
done=False

edge=[]

def getTile(p):
	return world.grid[p[0]][p[1]]

def dist(a,b):
	return abs(a[0]-b[0])+abs(a[1]-b[1])

def offset(p,x,y):
	return [p[0]+x,p[1]+y]

def offsety(p,y):
	return [p[0],p[1]+y]

def offsetx(p,x):
	return [p[0]+x,p[1]]
	
def match(a,b):
	if a[0] != b[0]:
		return False
	if a[1] != b[1]:
		return False
	return True
	
def free(x):
	tile=world.grid[x[0]][x[1]]
	if tile.wall:
		return False
	if tile.visited:
		return False
	return True
	
def visit(x,p):
	t=world.grid[x[0]][x[1]]
	t.visited=True
	t.aDist=world.grid[p[0]][p[1]].aDist+1
	
def expandEdge(x):
	t=edge.pop(x)
	new=[]
	p=offsetx(t,1)
	if free(p):
		new.append(p)
		
	p=offsetx(t,-1)
	if free(p):
		new.append(p)
	
	p=offsety(t,1)
	if free(p):
		new.append(p)
		
	p=offsety(t,-1)
	if free(p):
		new.append(p)
	
	for c in new:
		visit(c,t)
		if match(c,world.b):
			global done
			done=True
			return
		elif not match(c,world.a):
			r.renderCordTile(c)
	edge.extend(new)
	
	
def closestEdge():
	#global edge
	closest=0
	d=dist(edge[closest],world.b)
	for c in range(len(edge)):
		d2=dist(edge[c],world.b)
		if d2 < d:
			d=d2
			closest=c
	return closest;
	
def pathNextTile(t):
	n=t
	y=getTile(t)
	
	p=offsetx(t,1)
	x=getTile(p)
	if x.visited:
		n=p
		y=x
		
	p=offsetx(t,-1)
	x=getTile(p)
	if x.visited:
		if x.aDist < y.aDist:
			n=p
			y=x
	
	p=offsety(t,1)
	x=getTile(p)
	if getTile(p).visited:
		if x.aDist < y.aDist:
			n=p
			y=x
		
	p=offsety(t,-1)
	x=getTile(p)
	if getTile(p).visited:
		if x.aDist < y.aDist:
			n=p
			y=x
	
	return n

def findpath():
	global edge
	global done
	global delay
	done=False
	edge=[world.a]
	world.grid[world.a[0]][world.a[1]].visited=True
	#steps=0
	#find forward
	
	while not done:
		closest=closestEdge()
		expandEdge(closest)
		
		#display and delay
		#r.renderpoints()
		pygame.display.update()
		pygame.time.wait(delay)
		#steps+=1
		
	#pathback
	p=world.b
	for c in range(getTile(p).aDist-1):
		p=pathNextTile(p)
		if match(p,world.a):
			break#necessary for some rare cases
		r.pathBackTileRender(p)
		pygame.display.update()
		pygame.time.wait(delay)
	#r.renderpoints()
	#print(steps)
