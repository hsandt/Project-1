# -*-coding:Latin-1 -*

import os, sys
import pygame
import globals
from models import map, character, projectile
# from pygame.locals import * # pourrait être toléré
from constants import NB_SQUARES_PER_ROW, NB_SQUARES_PER_COL, SQUARE_SIDE # a-t-on mieux ?

def main():
	"""initialise les modèles puis gère les évènements et construit la vue dans une boucle
	à venir : gestion des gamestates

	"""
	pygame.init()
	# globals.init()

	# définition de l'écran de par sa taille : sera modifiée plus tard
	screen = pygame.display.set_mode((NB_SQUARES_PER_ROW * SQUARE_SIDE, NB_SQUARES_PER_COL * SQUARE_SIDE))

	# création de la map
	globals.map = map.Map('map.txt')

	# création du hero
	globals.hero = character.Character(image_path = 'charset1.png', position = [50, 50], max_life = 0, atk = 0, max_speed = 2)
	screen.blit(globals.hero.image,(0,0))
	
	# create dragon
	Dragon_Group=pygame.sprite.Group()
	for k in range(6):
		Dragon_Group.add(projectile.Balle(k*20,70*k,0))
		
	
	pygame.display.flip()

	
	globals.keyPressed = {'up': False, 'down': False, 'left': False, 'right': False}
	clock = pygame.time.Clock()

	while 1:
		# fpsClock=pygame.time.Clock()

		for event in pygame.event.get():

			# if event.type == pygame.KEYDOWN:
			# 	print("key_down")

			is_key_down = True if event.type == pygame.KEYDOWN else False
			if is_key_down or event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					globals.keyPressed['up'] = is_key_down
				elif event.key == pygame.K_DOWN:
					globals.keyPressed['down'] = is_key_down
				elif event.key == pygame.K_LEFT:
					globals.keyPressed['left'] = is_key_down
				elif event.key == pygame.K_RIGHT:
					globals.keyPressed['right'] = is_key_down

			if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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
