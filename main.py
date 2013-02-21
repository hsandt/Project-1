import os, sys
import pygame
import globals
from MapExtGroup import *
from personnage import *
from pygame.locals import *
from constants import *
from Projectile import *
from hero import *

def main():
	"main function of the game: initialize models, process events, draw the view"
	pygame.init()
	# globals.init()
	# screen size won't be defined this way later, but gives a good idea
	screen = pygame.display.set_mode((NB_CASES_PER_ROW*CASE_SIZE, NB_CASES_PER_COL*CASE_SIZE))

	# # dark gray background
	# background = pygame.Surface(screen.get_size())
	# background = background.convert()
	# background.fill((20,20,20))

	# create a Map object (inheriting from Group) from the filename
	globals.map = Map('ExempleMap.txt')

	# create hero
	globals.hero = Hero(image_path = 'charset1.png', position = [10, 10], max_life = 0, atk = 0, max_speed = 2)
	screen.blit(globals.hero.image,(0,0))
	
	#create dragon
	Dragon_Group=pygame.sprite.Group()
	for k in range(6):
                Dragon_Group.add(Balle(k*20,70*k,0))
	
	
	pygame.display.flip()

	
	globals.keyPressed = {'up': False, 'down': False, 'left': False, 'right': False}
	clock = pygame.time.Clock()

	while 1:
		# fpsClock=pygame.time.Clock()

		for event in pygame.event.get():

			if event.type == pygame.KEYDOWN:
				print("key_down")
			is_key_down = True if event.type == pygame.KEYDOWN else False
			if is_key_down or event.type == KEYUP:
				if event.key == K_UP:
					globals.keyPressed['up'] = is_key_down
				elif event.key == K_DOWN:
					globals.keyPressed['down'] = is_key_down
				elif event.key == K_LEFT:
					globals.keyPressed['left'] = is_key_down
				elif event.key == K_RIGHT:
					globals.keyPressed['right'] = is_key_down

			if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
				return

		globals.hero.update()
		
                        

		screen.fill((0,0,0))
		
                        
		globals.map.draw(screen) # Group method: rects for blitting are precised in the sprites of the group
		Dragon_Group.update()
		Dragon_Group.draw(screen)
		screen.blit(globals.hero.image,globals.hero.position)
		pygame.display.flip()
		# fpsClock.tick(100)
		clock.tick(globals.FPS)
		

if __name__ == '__main__': main()
