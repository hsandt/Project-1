# -*- coding: utf-8 -*-

import os, sys
import pygame
import globals

from gamestates.gamestate import GameContext, GameState, MenuState, ActionState

def main():

    """initialise les modeles puis gere les evenements et construit la vue dans une boucle

    """
    pygame.init()

    screen = pygame.display.set_mode((globals.NB_SQUARES_PER_ROW * globals.SQUARE_SIDE, globals.NB_SQUARES_PER_COL * globals.SQUARE_SIDE))

    # Création du game context et des games states associés
    gc = GameContext()

    clock = pygame.time.Clock()
    while 1:
        gc.handle_events()
        next_state = gc.update()
        gc.render(screen)
        pygame.display.flip()       #a placer après le changement éventuel de gamestate

        if not next_state == "keep":
            # quitter si la valeur de renvoi était nulle
            # à remplacer par un état d'exit en cours...
            if next_state == "exit":
                return
            gc.change_state(next_state)

        clock.tick(globals.FPS)
        # pygame.display.flip()

if __name__ == '__main__': main()
