import world as w
import render as r
import pygame

#1000= 1 second
delay=20

world=0#placeholder, set in main.py
done=False

edge=[]

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
	
def visit(x):
	world.grid[x[0]][x[1]].visited=True
	
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
		if match(c,world.b):
			global done
			done=True
			return
		else:
			visit(c)
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

def findpath():
	global edge
	global done
	global delay
	done=False
	edge=[world.a]
	#steps=0
	while not done:
		closest=closestEdge()
		expandEdge(closest)
		
		#display and delay
		r.renderpoints()
		pygame.display.update()
		pygame.time.wait(delay)
		#steps+=1
	#print(steps)
