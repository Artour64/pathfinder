import pygame
import render as r
import pathfinder as p
running=True

def event(event):
	if event.type == pygame.QUIT:
		global running
		running = False
	# key control
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_SPACE:#regen map
			r.world.worldGen()
			r.world.randpoints()
			r.renderTick()
		elif event.key == pygame.K_RETURN:
			r.renderTick()
			p.findpath()
			r.renderTick()
			r.world.worldGen()
			r.world.randpoints()
		
	#if event.type == pygame.KEYUP:
	#	pass
		
		#if event.key == pygame.K_LEFT:
		#	print("Left key released")
		#elif event.key == pygame.K_RIGHT:
		#	print("Right key released")
