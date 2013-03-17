# -*-coding:Latin-1 -*

import os, sys
import pygame
import globals
from models import map, character, projectile, building
# from pygame.locals import * # pourrait être toléré
from constants import NB_SQUARES_PER_ROW, NB_SQUARES_PER_COL, SQUARE_SIDE # a-t-on mieux ?

from gamestates.gameState import GameContext, GameState, MenuState, ActionState

def main():
	"""initialise les modèles puis gère les évènements et construit la vue dans une boucle
	à venir : gestion des gamestates

	"""
	pygame.init()
	# globals.init()

	# définition de l'écran de par sa taille : sera modifiée plus tard
	screen = pygame.display.set_mode((NB_SQUARES_PER_ROW * SQUARE_SIDE, NB_SQUARES_PER_COL * SQUARE_SIDE))

	# test game states
	gc = GameContext()

	clock = pygame.time.Clock()
	while 1:
		gc.handle_events()
		next_state = gc.update()
		gc.render(screen)
		pygame.display.flip()

		# quitter si la valeur de renvoi était nulle
		# à remplacer par un état d'exit en cours...
		if not next_state == "keep":
			if next_state == "exit":
				return
			gc.change_state(next_state)
		clock.tick(globals.FPS)


	# # création de la map
	# globals.map = map.Map('map.txt')

	# # création du hero
	# globals.hero = character.Character(image_path = 'charset1.png', position = [50, 50], max_life = 0, atk = 0, max_speed = 2)
	# screen.blit(globals.hero.image,(0,0))
	
	# # création du dragon
	# globals.balles=pygame.sprite.Group()

	# # creation des tours
	# globals.towers=pygame.sprite.Group()
	# globals.towers.add(building.Tour(15*32,5*32))


	# # création de la base
	# globals.base = building.Base(9*32,4*32)
		
	
	pygame.display.flip()

	
	# globals.keyPressed = {'up': False, 'down': False, 'left': False, 'right': False}
	# clock = pygame.time.Clock()

	# while 1:
	# 	# fpsClock=pygame.time.Clock()

	# 	for event in pygame.event.get():

			# if event.type == pygame.KEYDOWN:
			# 	print("key_down")

			# is_key_down = True if event.type == pygame.KEYDOWN else False

			# # tower number 0 shoots on space bar pressed
			# if is_key_down:
			# 	if event.key == pygame.K_SPACE:
			# 		globals.towers.sprites()[0].shoot(0)

			# if is_key_down or event.type == pygame.KEYUP:
			# 	if event.key == pygame.K_UP:
			# 		globals.keyPressed['up'] = is_key_down
			# 	elif event.key == pygame.K_DOWN:
			# 		globals.keyPressed['down'] = is_key_down
			# 	elif event.key == pygame.K_LEFT:
			# 		globals.keyPressed['left'] = is_key_down
			# 	elif event.key == pygame.K_RIGHT:
			# 		globals.keyPressed['right'] = is_key_down

			# if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			# 	return

		# globals.hero.update()
		# globals.balles.update()



		# screen.fill((0,0,0))
		

		# globals.map.draw(screen) # Group method: rects for blitting are precised in the sprites of the group
		
		# globals.balles.draw(screen)
		# globals.towers.draw(screen)
		# screen.blit(globals.hero.image,globals.hero.position)
		# screen.blit(globals.base.image,globals.base.rect)
		
		# pygame.display.flip()

		# clock.tick(globals.FPS)
		

if __name__ == '__main__': main()
