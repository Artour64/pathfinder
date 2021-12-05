import pygame
pygame.init()


import world as w
world = w.World()
#world.makeGrid(3,2)
world.worldGen()
world.randpoints()

import render as r
r.world=world
r.renderInit()
r.renderFirst()


import pathfinder as p
p.world=world

import events as ev
while ev.running:
	for event in pygame.event.get():
		ev.event(event)
    
