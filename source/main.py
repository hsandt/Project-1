# -*-coding:Latin-1 -*

import os, sys
import pygame
import globals

from gamestates.gameState import GameContext, GameState, MenuState, ActionState

def main():
	"""initialise pygame, l'écran, le game context, puis lance la boucle de jeu

	"""
	pygame.init()
	# globals.init()

	# définition de l'écran de par sa taille : sera modifiée plus tard
	screen = pygame.display.set_mode((globals.NB_SQUARES_PER_ROW * globals.SQUARE_SIDE, globals.NB_SQUARES_PER_COL * globals.SQUARE_SIDE))

	# test game states
	gc = GameContext()

	clock = pygame.time.Clock()
	while 1:
		gc.handle_events()
		next_state = gc.update()
		gc.render(screen)
		pygame.display.flip()

		if not next_state == "keep":
			# quitter si la valeur de renvoi était nulle
			# à remplacer par un état d'exit en cours...
			if next_state == "exit":
				return
			gc.change_state(next_state)

		clock.tick(globals.FPS)
	
if __name__ == '__main__': main()
